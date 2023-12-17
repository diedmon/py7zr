import py7zr
import pytest

@pytest.mark.empty_stream
def test_empty_stream(self):
  try:
    with py7zr.SevenZipFile(file="test.7z",mode="w") as archive:
      archive.writestr(data="",arcname="empty.txt")
  except:
    pytest.fail("Exception raised")
