def line_count():
  # Defines file and open's and reads 'file.txt'
  file = open('file.txt', 'r')
  # Defines lines and sets lines equal to the length of lines in file
  lines = len(file.readlines())
  # This closes the file after it is done defining the length of lines
  file.close()
  # Returns the value of lines 
  return lines