import py7zr

def test_empty_stream():
  try:
    with py7zr.SevenZipFile(file="test.7z",mode="w") as archive:
      archive.writestr(data="",arcname="empty.txt")
  except:
    self.fail("Exception raised")
