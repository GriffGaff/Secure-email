import config

def load_blacklist():
    with open(config.BLACKLIST_FILE, "r") as file:
        return set(line.strip() for line in file.readlines())

def is_blacklisted(sender):
    blacklist = load_blacklist()
    return sender in blacklist
