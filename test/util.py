import tempfile, os

MODE = 0

def make_tempfile_with_content(content):
    tfile = tempfile.NamedTemporaryFile(delete=False).name
    with open(tfile, "w") as f:
        f.write(content)
    return tfile

def delete_tempfile(fname):
    os.unlink(fname)