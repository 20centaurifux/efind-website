import os, hashlib

def md5(name):
	hash_md5 = hashlib.md5()

	with open(name, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)

	return hash_md5.hexdigest()

def build_download_name(name, filename):
	if name == "source":
		return "Source code"

	if name == "arch":
		name = name.title()
	elif name == "centos-7":
		name = "CentOS 7"
	elif name == "debian-8":
		name = "Debian 8"
	elif name == "debian-9":
		name = "Debian 9"
	elif name == "fedora-25":
		name = "Fedora 25"
	elif name == "opensuse-leap":
		name = "openSUSE Leap 42.2"
	elif name == "slackware-14.2":
		name = "Slackware 14.2"
	elif name == "ubuntu-16.04":
		name = "Ubuntu 16.04"
	elif name == "ubuntu-17.04":
		name = "Ubuntu 17.04"

	if "x86_64" in filename or "amd64" in filename:
		name = "%s (64-bit)" % name
	else:
		name = "%s (32-bit)" % name

	return name

def generate_rows(subfolder, pkg, version):
	for filename in sorted(os.listdir("docs/downloads/%s" % subfolder)):
		prefix0 = "%s-%s" % (pkg, version)
		prefix1 = "%s_%s" % (pkg, version)

                offset = 0

                if pkg != "efind":
                    offset += 1

		pos = prefix1.rfind('.')
		prefix1 = "%s-%d" % (prefix1[:pos], int(prefix1[pos + 1:]) + offset)

		if (filename.startswith(prefix0) or filename.startswith(prefix1)) and not filename.endswith(".asc"):
			print "%s|[%s](downloads/%s/%s)|%s|[Signature](downloads/%s/%s.asc)" % (build_download_name(subfolder, filename), filename, subfolder, filename, md5("docs/downloads/%s/%s" % (subfolder, filename)), subfolder, filename)

def generate_table(pkg, version):
	print "| Download | Link | MD5 | GPG |"
	print "| :------- | :--- | :-- | :-- |"

	generate_rows("source", pkg, version)

        for filename in sorted(os.listdir("docs/downloads")):
		if filename <> "source":
			generate_rows(filename, pkg, version)

with open("downloads.head.md") as f:
    print f.read()

print "##efind\n"
generate_table("efind", "0.2.2")

print "\n##gdkpixbuf extension\n\nFilter search results by image properties.\n"
generate_table("efind-gdkpixbuf", "0.1.1")

print "\n##taglib extension\n\nFilter search results by audio tags and properties.\n"
generate_table("efind-taglib", "0.1.1")

with open("downloads.tail.md") as f:
    print "\n%s" % f.read()
