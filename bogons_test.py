import bogons
import unittest


class valid_public_asnTest(unittest.TestCase):
    def test_valid_public_asn(self):
        self.assertEqual(bogons.valid_public_asn(-1), False)
        self.assertEqual(bogons.valid_public_asn(0), False)
        self.assertEqual(bogons.valid_public_asn(1), True)
        self.assertEqual(bogons.valid_public_asn(23456), False)
        self.assertEqual(bogons.valid_public_asn(64496), False)
        self.assertEqual(bogons.valid_public_asn(64511), False)
        self.assertEqual(bogons.valid_public_asn(64512), False)
        self.assertEqual(bogons.valid_public_asn(65534), False)
        self.assertEqual(bogons.valid_public_asn(65535), False)
        self.assertEqual(bogons.valid_public_asn(65551), False)
        self.assertEqual(bogons.valid_public_asn(131071), False)
        self.assertEqual(bogons.valid_public_asn(4199999999), True)
        self.assertEqual(bogons.valid_public_asn(4200000000), False)
        self.assertEqual(bogons.valid_public_asn(4294967295), False)
        self.assertEqual(bogons.valid_public_asn(18446744073709551615), False)
        self.assertEqual(bogons.valid_public_asn("word"), False)

    def test_is_public_ipv4(self):
        self.assertEqual(bogons.is_public_ipv4("0.0.0.1"), False)
        self.assertEqual(bogons.is_public_ipv4("1.1.1.1"), True)
        self.assertEqual(bogons.is_public_ipv4("10.1.1.1"), False)
        self.assertEqual(bogons.is_public_ipv4("11.1.1.1"), True)
        self.assertEqual(bogons.is_public_ipv4("11.1.1.1.1"), False)
        self.assertEqual(bogons.is_public_ipv4("172.16.1.1"), False)
        self.assertEqual(bogons.is_public_ipv4("100.64.0.1"), False)
        self.assertEqual(bogons.is_public_ipv4("100.127.0.0"), False)
        self.assertEqual(bogons.is_public_ipv4("169.254.10.1"), False)
        self.assertEqual(bogons.is_public_ipv4("192.0.0.1"), False)
        self.assertEqual(bogons.is_public_ipv4("192.0.1.1"), True)
        self.assertEqual(bogons.is_public_ipv4("192.0.2.1"), False)
        self.assertEqual(bogons.is_public_ipv4("192.168.1.1"), False)
        self.assertEqual(bogons.is_public_ipv4("193.168.1.1"), True)
        self.assertEqual(bogons.is_public_ipv4("198.18.100.2"), False)
        self.assertEqual(bogons.is_public_ipv4("198.51.100.2"), False)
        self.assertEqual(bogons.is_public_ipv4("203.0.113.2"), False)
        self.assertEqual(bogons.is_public_ipv4("224.168.1.1"), False)
        self.assertEqual(bogons.is_public_ipv4("🎈"), False)

    def test_is_public_ipv6(self):
        self.assertEqual(bogons.is_public_ipv6("2001:0:1:2::3"), False)
        self.assertEqual(bogons.is_public_ipv6("2001:1:2::3"), False)
        self.assertEqual(bogons.is_public_ipv6("2001:db8:1:2::3"), False)
        self.assertEqual(bogons.is_public_ipv6("2002:b8:1:2::3"), False)
        self.assertEqual(bogons.is_public_ipv6("2600::"), True)
        self.assertEqual(bogons.is_public_ipv6("3ffe::"), False)
        self.assertEqual(bogons.is_public_ipv6("3fff::"), True)
        self.assertEqual(bogons.is_public_ipv6("3fff:::"), False)
        self.assertEqual(bogons.is_public_ipv6("4600::"), False)
        self.assertEqual(bogons.is_public_ipv6(""), False)
        self.assertEqual(bogons.is_public_ipv6("🎈"), False)
