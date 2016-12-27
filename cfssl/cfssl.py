# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import requests

from .exceptions import CFSSLException, CFSSLRemoteException

from .models.config_key import ConfigKey


class CFSSL(object):
    """ It provides Python bindings to a remote CFSSL server via HTTP(S).

    Additional documentation regarding the API endpoints is available at
    https://github.com/cloudflare/cfssl/tree/master/doc/api
    """

    def __init__(self, host, port, ssl=True, verify_cert=True):
        """ Initialize the CFSSL object.

        Args:
            host (str): Host or IP of remote CFSSL instance.
            port (int): Port number of remote CFSSL instance.
            ssl (bool): Whether to use SSL.
            verify_cert (bool or str): File path of CA cert for verification,
                `True` to use system certs, or `False` to disable certificate
                verification.
        """
        ssl = 'https' if ssl else 'http'
        self.verify = verify_cert
        self.uri_base = '%s://%s:%d' % (ssl, host, port)

    def auth_sign(self, token, request, datetime=None, remote_address=None):
        """ It provides returns a signed certificate.

        Args:
            token (str): The authentication token.
            request (CertificateRequest): Signing request document.
            datetime (datetime.datetime): Authentication timestamp.
            remote_address (str): An address used in making the request.
        Returns:
            str: A PEM-encoded certificate that has been signed by the
                server.
        """
        data = self._clean_mapping({
            'token': token,
            'request': request.to_api(),
            'datetime': datetime,
            'remote_address': remote_address,
        })
        return self.call('authsign', 'POST', data=data)

    def bundle(self, certificate, private_key=None,
               flavor='ubiquitous', domain=None, ip=None):
        """ It builds and returns certificate bundles.

        Args:
            certificate (str): The PEM-encoded certificate to be bundled.

        If the ``certificate`` parameter is present, the following four
        arguments are valid:
            private_key (str): The PEM-encoded private key to be included with
                the bundle. This is valid only if the server is not running in
                ``keyless`` mode.
            flavor (str): One of ``ubiquitous``, ``force``, or ``optimal``,
                with a default value of ``ubiquitous``. A ubiquitous bundle is
                one that has a higher probability of being verified everywhere,
                even by clients using outdated or unusual trust stores. Force will
                cause the endpoint to use the bundle provided in the
                ``certificate`` parameter, and will only verify that the bundle
                is a valid (verifiable) chain.
            domain (str): The domain name to verify as the hostname of the
                certificate.
            ip (str): The IP address to verify against the certificate IP
                SANs.

        If only the ``domain`` parameter is present, the following
        parameter is valid:

        ip (str): The IP address of the remote host; this will fetch the
            certificate from the IP, and verify that it is valid for the
            domain name.

        Returns:
            dict: Object representing the bundle, with the following keys:
                * bundle contains the concatenated list of PEM certificates
                  forming the certificate chain; this forms the actual
                  bundle. The remaining parameters are additional metadata
                  supporting the bundle.
                * crl_support is true if CRL information is contained in the
                  certificate.
                * crt contains the original certificate the bundle is built
                  from.
                * expires contains the expiration date of the certificate.
                * hostnames contains the SAN hostnames for the certificate.
                * issuer contains the X.509 issuer information for the
                  certificate.
                * key contains the private key for the certificate, if one
                  was presented.
                * key_size contains the size of the key in bits for the
                  certificate. It will be present even if the private key wasn't
                  provided because this can be determined from the public key.
                * key_type contains a textual description of the key type,
                  e.g. '2048-bit RSA'.
                * ocsp contains the OCSP URLs for the certificate, if present.
                * ocsp_support will be true if the certificate supports OCSP
                  revocation checking.
                * signature contains the signature type used in the
                  certificate, e.g. ``SHA1WithRSA``.
                * status contains a :type:`dict` of elements:
                  * code is bit-encoded error code. 1st bit indicates whether
                    there is a expiring certificate in the bundle. 2nd bit indicates
                    whether there is a ubiquity issue with the bundle.
                  * expiring_SKIs contains the SKIs (subject key identifiers)
                    for any certificates that might expire soon (within 30
                    days).
                  * messages is a list of human-readable warnings on bundle
                    ubiquity and certificate expiration. For example, an expiration
                    warning can be "The expiring cert is #1 in the chain",
                    indicating the leaf certificate is expiring. Ubiquity warnings
                    include SHA-1 deprecation warning (if the bundle triggers
                    any major browser's SHA-1 deprecation policy), SHA-2
                    compatibility warning (if the bundle contains signatures using
                    ECDSA SHA-2 hash algorithms, it will be rejected by Windows XP
                    SP2), compatibility warning (if the bundle contains ECDSA
                    certificates, it will be rejected by Windows XP, Android 2.2 and
                    Android 2.3 etc) and root trust warning (if the bundle cannot be
                    trusted by some major OSes or browsers).
                  * rebundled indicates whether the server had to rebundle the
                    certificate. The server will rebundle the uploaded
                    certificate as needed; for example, if the certificate
                    contains none of the required intermediates or a better set
                    of intermediates was found. In this case, the server will
                    mark rebundled as true.
                  * untrusted_root_stores contains the names of any major
                    OSes and browsers that doesn't trust the bundle. The names
                    are used to construct the root trust warnings in the messages
                    list
                * subject contains the X.509 subject identifier from the
                    certificate.
        """
        data = self._clean_mapping({
            'certificate': certificate,
            'domain': domain,
            'private_key': private_key,
            'flavor': flavor,
            'ip': ip,
        })
        return self.call('bundle', 'POST', data=data)

    def info(self, label, profile=None):
        """ It returns information about the CA, including the cert.

        Args:
            label (str): A string specifying the signer.
            profile (str): a string specifying the signing profile for the
                signer. Signing profile specifies what key usages should be
                used and how long the expiry should be set.
        Returns:
            dict: Mapping with three keys:
                * certificate (str): a PEM-encoded certificate of the signer.
                * usage (list of str): Key usages from the signing
                    profile.
                * expiry (str): the expiry string from the signing profile.
        """
        data = self._clean_mapping({
            'label': label,
            'profile': profile,
        })
        return self.call('info', 'POST', data=data)

    def init_ca(self, certificate_request, ca=None):
        """ It initializes a new certificate authority.

        Args:
            certificate_request (CertificateRequest): The certificate
                request to use when creating the CA.
            ca (ConfigServer, optional): The configuration of the
                requested Certificate Authority.
        Returns:
            dict: Mapping with two keys:
                * private key (str): a PEM-encoded CA private key.
                * certificate (str): a PEM-encoded self-signed CA certificate.
        """
        csr_api = certificate_request.to_api()
        data = self._clean_mapping({
            'hosts': csr_api['hosts'],
            'names': csr_api['names'],
            'CN': csr_api['CN'],
            'key': csr_api['key'],
            'ca': ca and ca.to_api() or None,
        })
        return self.call('init_ca', 'POST', data=data)

    def new_key(self, hosts, names, common_name=None, key=None, ca=None):
        """ It generates and returns a new private key + CSR.

        Args:
            hosts (tuple of Host): Subject Alternative Name(s) for the
                requested certificate.
            names (tuple of SubjectInfo): The Subject Info(s) for the
                requested certificate.
            CN (str): the common name for the certificate subject in the
                requestedrequested CA certificate.
            key (ConfigKey): Cipher and strength to use for certificate.
            ca (ConfigServer): the CA configuration of the requested CA.
        Returns:
            dict: Mapping with three keys:
                * private key (str): a PEM-encoded CA private key.
                * certificate (str): a PEM-encoded self-signed CA certificate.
                * sums (dict): Mapping holding both MD5 and SHA1 digests for
                  the certificate request
        """
        data = self._clean_mapping({
            'hosts': [
                host.to_api() for host in hosts
            ],
            'names': [
                name.to_api() for name in names
            ],
            'CN': common_name,
            'key': key and key.to_api() or ConfigKey().to_api(),
            'ca': ca and ca.to_api() or None,
        })
        return self.call('newkey', 'POST', data=data)

    def new_cert(self, request, label=None, profile=None, bundle=None):
        """ It generates and returns a new private key and certificate.

        Args:
            request (CertificateRequest): CSR to be used for
                certificate creation.
            label (str): Specifying which signer to be appointed to sign
                the CSR, useful when interacting with cfssl server that stands
                in front of a remote multi-root CA signer.
            profile (str): Specifying the signing profile for the signer.
            bundle (bool): Specifying whether to include an "optimal"
                certificate bundle along with the certificate.
        Returns:
            dict: mapping with these keys:
                * private key (str): a PEM-encoded private key.
                * certificate_request (str): a PEM-encoded certificate request.
                * certificate (str): a PEM-encoded certificate, signed by the server.
                * sums (dict): Holding both MD5 and SHA1 digests for the
                    certificate request and the certificate.
                * bundle (str): See the result of endpoint_bundle.txt (only included
                    if the bundle parameter was set).
        """
        data = self._clean_mapping({
            'request': request.to_api(),
            'label': label,
            'profile': profile,
            'bundle': bundle,
        })
        return self.call('newcert', 'POST', data=data)

    def revoke(self, serial, authority_key_id, reason):
        """ It provides certificate revocation.

        Args:
            serial (str): Specifying the serial number of a certificate.
            authority_key_id (str): Specifying the authority key identifier
                of the certificate to be revoked; this is used to distinguish
                which private key was used to sign the certificate.
            reason (str): Identifying why the certificate was revoked; see,
                for example, ReasonStringToCode in the ocsp package or section
                4.2.1.13 of RFC 5280. The "reasons" used here are the ReasonFlag
                names in said RFC.
        """
        data = self._clean_mapping({
            'serial': serial,
            'authority_key_id': authority_key_id,
            'reason': reason,
        })
        return self.call('revoke', 'POST', data=data)

    def scan(self, host, ip=None, timeout=None, family=None, scanner=None):
        """ It scans servers to determine the quality of their TLS setup.

        Args:
            host (Host): The host to scan.
            ip (str): IP Address to override DNS lookup of host.
            timeout (str): The amount of time allotted for the scan to complete
                (default: 1 minute).
            family (str): regular expression specifying scan famil(ies) to run.
            scanner (str): regular expression specifying scanner(s) to run.
        Returns:
            dict: Mapping with keys for each scan family. Each of these
            objects contains keys for each scanner run in that family 
            pointing to objects possibly containing the following keys:
            * grade (str): Describing the exit status of the scan. Can be:
                * "Good": host performing the expected state-of-the-art.
                * "Warning": host with non-ideal configuration,
                             possibly maintaining support for legacy clients.
                * "Bad": host with serious misconfiguration or vulnerability
                * "Skipped": indicates that the scan was not performed for some
                             reason.
            * error (str): Any error encountered during the scan process.
            * output: (dict) Arbitrary data retrieved during the scan.
        """
        data = self._clean_mapping({
            'host': host.to_api(),
            'ip': ip,
            'timeout': timeout,
            'family': family,
            'scanner': scanner,
        })
        return self.call('scan', params=data)

    def scan_info(self):
        """ It lists options available for scanning.

        Returns:
            dict: Mapping with keys for each scan family. For each family,
                there exists a `description` containing a string describing
                the family and a `scanners` object mapping each of the family's
                scanners to an object containing a `description` string.
        """
        return self.call('scaninfo')

    def sign(self, certificate_request, hosts=None, subject=None,
             serial_sequence=None, label=None, profile=None):
        """ It signs and returns a certificate.

        Args:
            certificate_request (str): the CSR bytes to be signed (in PEM).
            hosts (tuple of Host): of SAN (subject alternative .names)
                which overrides the ones in the CSR
            subject (str): The certificate subject which overrides
                the ones in the CSR.
            serial_sequence (str): Specify the prefix which the generated
                certificate serial should have.
            label (str): Specifying which signer to be appointed to sign
                the CSR, useful when interacting with a remote multi-root CA
                signer.
            profile (ConfigServer): Specifying the signing profile for
                the signer, useful when interacting with a remote multi-root
                CA signer.
        Returns:
            str: A PEM-encoded certificate that has been signed by the
                server.
        """
        data = self._clean_mapping({
            'certificate_request': certificate_request.to_api(),
            'hosts': [
                host.to_api() for host in hosts
            ],
            'subject': subject,
            'serial_sequence': serial_sequence,
            'label': label,
            'profile': profile.to_api(),
        })
        result = self.call('sign', 'POST', data=data)
        return result['certificate']

    def call(self, endpoint, method='GET', params=None, data=None):
        """ It calls the remote endpoint and returns the result, if success.

        Args:
            endpoint (str): CFSSL endpoint to call (e.g. ``newcert``).
            method (str): HTTP method to utilize for the Request.
            params: (dict|bytes) Data to be sent in the query string
                for the Request.
            data: (dict or bytes or file) Data to send in the body
                of the Request.
        Returns:
            (mixed) Data contained in ``result`` key of the API response.
        Raises:
            CFSSLRemoteException: In the event of a ``False`` in the
                ``success`` key of the API response.
        """
        endpoint = '%s/api/v1/cfssl/%s' % (self.uri_base, endpoint)
        response = requests.request(
            method=method,
            url=endpoint,
            params=params,
            data=data,
            verify=self.verify,
        )
        response = response.json()
        if not response['success']:
            raise CFSSLRemoteException(
                '\n'.join([
                    'Errors:',
                    '\n'.join(response.get('errors', [])),
                    'Messages:'
                    '\n'.join(response.get('messages', [])),
                ])
            )
        return response['result']

    def _clean_mapping(self, mapping):
        """ It removes false entries from mapping """
        return {k:v for k, v in mapping.iteritems() if v}
