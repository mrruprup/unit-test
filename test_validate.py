from validate import Validate    # The code to test
import unittest   # The test framework

class Test_TestValidate(unittest.TestCase):
    def test_zip_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.zip("17701"))

    def test_zip_bad(self):
        #ABUSE
        f = open("blns.txt", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.zip(str(line)))

    def test_minor_happy(self):
        #HAPPY PATH
        good_vals = [1,2,10,11,12]
            
        for val in good_vals:
            print(f'testing {val}')
            self.assertTrue(Validate.minor(val))

    def test_minor_bad(self):
        #ABUSE
        f = open("blns.txt", "rb")
            
        for line in f:
            print(f'testing {line}')
            if line == "0" and line == "1":
                continue
            self.assertFalse(Validate.minor(str(line)))

    def test_email_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.email("email@example.com"))

    def test_email_bad(self):
        #ABUSE
        f = open("blns.txt", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.email(str(line)))

    def test_lat_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.is_lat("45.0"))

    def test_lat_bad(self):
        #ABUSE
        f = open("blns.txt", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.is_lat(str(line)))

    def test_long_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.is_long("100.0"))

    def test_long_bad(self):
        #ABUSE
        f = open("blns.txt", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.is_long(str(line)))

    def test_domain_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.is_domain("example.com"))

    def test_domain_bad(self):
        #ABUSE
        f = open("blns.txt", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.is_domain(str(line)))

    def test_url_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.is_url("http://example.com"))

    def test_url_bad(self):
        #ABUSE
        f = open("blns.txt", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.is_url(str(line)))

    def test_grade_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.grade(85))

    def test_grade_bad(self):
        #ABUSE
        f = open("blns.txt", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.grade(str(line)))

    def test_good_sql(self):
        #HAPPY PATH
        self.assertTrue(Validate.sanitize("SELECT * FROM users"))

    def test_bad_sql(self):
        #ABUSE
        f = open("blns.txt", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.sanitize(str(line)))
    
    def test_no_sql_injection_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.no_sql_injection("hello world"))
    
    def test_no_sql_injection_bad(self):
        #ABUSE
        f = open("blns.txt", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.no_sql_injection(str(line)))

    def test_strip_null(self):
        #HAPPY PATH
        test = ["hello\x00world", None, "hello\x00None\x00world"]

        sanitized = [Validate.strip_null(item) for item in test]

        print(sanitized[0], sanitized[1], sanitized[2])

    def test_strip_null_bad(self):
        #ABUSE
        f = open("blns.txt", "rb")

        for line in f:
            print(f"Attempting {line}")
            sanitized = Validate.strip_null(line)
            self.assertNotIn(b"None", sanitized)
            self.assertNotIn(b"\x00", sanitized)
    def test_ip_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.ip("168.192.1.3"))

    def test_ip_bad(self):
        #ABUSE
        f = open("blns.txt", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.ip(str(line)))
    def test_mac_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.mac(str("AA:BB:CC:DD:EE:FF")))

    def test_mac_bad(self):
        #ABUSE
        f = open("blns.txt", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.mac(str(line)))

    def test_md5_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.md5("d41d8cd98f00b204e9800998ecf8427e"))

    def test_md5_bad(self):
        #ABUSE
        f = open("blns.txt", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.md5(str(line)))

if __name__ == '__main__':
    unittest.main()