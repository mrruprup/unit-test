import re

class Validate:

  @staticmethod
  def zip(input):
    if re.match("^[0-9]{5}$", input):
      return True
    return False
  
  @staticmethod
  def minor(age):
    try:
      age = int(age)
      if age > 17:
        return False
      return True
    except Exception as e:
      #print(e)
      return False
  
  @staticmethod 
  def email(input):
    if re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", input):
      return True
    return False
  
  @staticmethod
  def is_lat(lat):
    try:
      lat = float(lat)
      return lat >= -90 and lat <= 90
    except (ValueError, TypeError) as e:
      #print(e)
      return False
  
  @staticmethod
  def is_long(long):
    try:
      long = float(long)
      return long >= -180 and long <= 180
    except (ValueError, TypeError) as e:
      #print(e)
      return False
  
  @staticmethod
  def is_domain(input):
    if re.match("^[a-zA-Z0-9-]{2,253}\\.[a-zA-Z]{1}[a-zA-Z0-9]{1,}$", input):
      return True
    return False
  
  @staticmethod
  def is_url(input):
      # regex obtained from https://uibakery.io/regex-library/url-regex-python
      if re.match("^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$", input):
        return True
      return False

  @staticmethod
  def grade(value):

    value = str(value).strip()
    #regex checks if this value is a number with two decimal places at most
    if not re.fullmatch("^\d+(\.\d{1,2})?", value):
        return False
    #convert the value back to a float
    value = float(value)

    if value < 0 or value > 100:
      raise ValueError("Value must be between 0 and 100")
  
    if value <= 59.99:
      grade = 'F'
      print(grade)
      return grade
    elif value <= 69.99:
      grade = 'D'
      print(grade)
      return grade
    elif value <= 79.99:
      grade = 'C'
      print(grade)
      return grade
    elif value <= 89.99:
      grade = 'B'
      print(grade)
      return grade
    
    grade = 'A'
    print(grade)
    return grade
  
  '''
  Typing added to enhance validation
  '''
  @staticmethod
  def sanitize(sql):
    #read only SQL

    sql = sql.strip()

    # if sql does not start with a select statement then return false
    if not sql.upper().startswith("SELECT"):
      return False
    # if sql contains any of the following characters then return false
    if re.search("--|#|/\*", sql):
      return False
    return True
  
  def no_sql_injection(input):
    # check if input contains any of the following characters
    if not re.match(r"^[a-zA-Z0-9 ]+$", input):
      return False
    if re.search("SELECT|INSERT|UPDATE|DELETE|DROP|ALTER|CREATE", input, re.IGNORECASE):
      return False
    return True
  
    
  @staticmethod
  def strip_null(input : str) -> str:
    if input == None:
      return ""
    if isinstance(input, bytes):
          # remove b"None" and null bytes
        sanitized = input.replace(b"None", b"").replace(b"\x00", b"")
    elif isinstance(input, str):
          # remove "None" and null bytes
        sanitized = input.replace("None", "").replace("\x00", "")
    else:
          # anything else, just return as-is
        sanitized = input
    return sanitized
  '''
  TODO: Implement IP validation. Consider white-list, regex.
  '''
  @staticmethod
  def ip(input : int) -> int:
    if re.match("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", input):
      return True
    return False
  
  '''
  TODO: Implement MAC address validation. Consider white-list, regex.

  allow : - and whitespaces
  '''
  @staticmethod
  def mac(input) -> bool:
    if re.match("^([0-9A-Fa-f]{2}[-]?[\:s]?){5}([0-9A-Fa-f]{2})$", input):
      return True
    return False

  '''
  TODO: Implement md5 validation. Consider white-list, regex.
  '''
  @staticmethod
  def md5(input) -> bool:
    if re.match("^[a-fA-F0-9]{32}$", input):
      return True
    return False