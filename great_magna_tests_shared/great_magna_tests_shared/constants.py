# -*- coding: utf-8 -*-
import os
from glob import glob

from envparse import env

MD5_CHECKSUM_EIG_LOGO = env.str(
   "EIG_LOGO_MD5_CHECKSUM", default="8bc6134cffb3cdb134ad910e6a698fb8"
)
MD5_CHECKSUM_GREAT_LOGO = env.str(
   "GREAT_LOGO_MD5_CHECKSUM", default="6af76ffaffc1009edc9f92871ce73274"
)
MD5_CHECKSUM_EVENTS_BIG_HEADER_LOGO = env.str(
   "EVENTS_BIG_LOGO_MD5_CHECKSUM", default="cf06c747729c8515086b39a47f149fad"
)
MD5_CHECKSUM_EVENTS_BIG_FOOTER_LOGO = env.str(
   "EVENTS_BIG_FOOTER_LOGO_MD5_CHECKSUM", default="7efc18df0076a860835196f7ca39e437"
)
MD5_CHECKSUM_INVEST_IN_GREAT = env.str(
   "MD5_CHECKSUM_INVEST_IN_GREAT", default="b1cca6e547c89896f0b13632bc298168"
)
MD5_CHECKSUM_DIT_FAVICON = env.str(
   "DIT_FAVICON_MD5_CHECKSUM", default="93bd34ac9de2cb059c65c5e7931667a2"
)

EMAIL_VERIFICATION_CODE_SUBJECT = "Your confirmation code for great.gov.uk"
EMAIL_VERIFICATION_MSG_SUBJECT = "Confirm your email address"
EMAIL_ERP_PROGRESS_SAVED_MSG_SUBJECT = "We’ve saved your progress until"
FAS_MESSAGE_FROM_BUYER_SUBJECT = (
    "New message through your great.gov.uk business profile"
)

# Absolute path to a directory with test images
test_files_path_current_dir = os.path.abspath(os.path.join(".", "files"))
test_files_path_browser_tests = os.path.abspath(os.path.join("..", "files"))
test_files_path_other_tests = os.path.abspath(os.path.join("tests", "files"))
if os.path.isdir(test_files_path_current_dir):
    TEST_IMAGES_DIR = test_files_path_current_dir
elif os.path.isdir(test_files_path_browser_tests):
    TEST_IMAGES_DIR = test_files_path_browser_tests
elif os.path.isdir(test_files_path_other_tests):
    TEST_IMAGES_DIR = test_files_path_other_tests
else:
    raise FileNotFoundError

# lists of absolute paths to test images of specific type
PNGs = glob(os.path.join(TEST_IMAGES_DIR, "*.png"))
JPGs = glob(os.path.join(TEST_IMAGES_DIR, "*.jpg"))
JPEGs = glob(os.path.join(TEST_IMAGES_DIR, "*.jpeg"))
BMPs = glob(os.path.join(TEST_IMAGES_DIR, "*.bmp"))
JP2s = glob(os.path.join(TEST_IMAGES_DIR, "*.jp2"))  # noqa
WEBPs = glob(os.path.join(TEST_IMAGES_DIR, "*.webp"))
#
# """
# Load a list of rare english words.
# This list was compiled using:
# a) Wictionary top 100,000 most frequently-used English words
#   -> https://gist.github.com/h3xx/1976236
# b) 20000 most common English words in order of frequency, as determined by
#   n-gram frequency analysis of the Google's Trillion Word Corpus
#   -> https://github.com/first20hours/google-10000-english/blob/master/20k.txt
#
# The selection process was as follows:
# 1) delete first 30000 lines from a)
# 2) select words with a least 9 characters: if len(w) > 8
# 3) skip all words that contain non-ASCII characters: len(w) == len(w.encode())
# 4) skip all words that contain non-latin alphabet characters, like: ',."@$ etc
#    skip = ["'", "\"", "`", ",", ".", ";", ":", "!", "#", "@", "$", "%", "^",
#            "&", "*", "(", ")", "-", "=", "+", "_", "{", "[", "]", "}", "?",
#            ">", "<"]
#    all(e not in w for e in skip)
# 5) make all words lower case: w.lower()
# 6) remove all duplicates: set(words)
# 7) sort
# 8) remove from selected words all words present in b)
#    grep -v -x -f 100k.txt 20k.txt > rare.txt
#
# Steps 2-7:
# with open("./100k.txt") as f:
#    words = f.read().split()
#
# skip = ["'", "\"", "`", ",", ".", ";", ":", "!", "#", "@", "$", "%", "^", "&",
#         "*", "(", ")", "-", "=", "+", "_", "{", "[", "]", "}", "?", ">", "<"]
# nine = sorted(set([w.lower() for w in words
#                    if len(w) > 8
#                    and len(w) == len(w.encode())
#                    and all(e not in w for e in skip)]))
# """
with open(os.path.join(TEST_IMAGES_DIR, "rare.txt"), "r") as f:
    RARE_WORDS = f.read().split()
#
# """
# This list
# PS.
# a) 20000 most common English words in order of frequency, as determined by
#   -> https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears-medium.txt
# """
with open(os.path.join(TEST_IMAGES_DIR, "english-4k.txt"), "r") as f:
    POPULAR_ENGLISH_WORDS = f.read().split()

SEPARATORS = {
    "pipe": "|",
    "semi-colon": ";",
    "colon": ":",
    "full stop": ".",
    "comma": ",",
}

OPERATING_COUNTRIES = [
   60,
   61,
   62,
   64,
   65,
   344,
   69,
   70,
   73,
   74,
   75,
   77,
   78,
   79,
   80,
   81,
   83,
   84,
   86,
   87,
   343,
   90,
   94,
   95,
   96,
   342,
   98,
   99,
   100,
   101,
   102,
   104,
   341,
   109,
   110,
   111,
   114,
   115,
   116,
   340,
   120,
   121,
   122,
   124,
   125,
   126,
   127,
   128,
   339,
   131,
   132,
   133,
   134,
   338,
   136,
   137,
   138,
   141,
   142,
   144,
   148,
   151,
   152,
   153,
   155,
   157,
   160,
   161,
   162,
   163,
   164,
   166,
   168,
   169,
   170,
   171,
   172,
   173,
   328,
   175,
   176,
   177,
   178,
   179,
   180,
   181,
   182,
   183,
   184,
   185,
   186,
   189,
   190,
   191,
   192,
   193,
   194,
   195,
   196,
   197,
   337,
   199,
   200,
   201,
   202,
   203,
   204,
   205,
   207,
   208,
   211,
   212,
   213,
   336,
   214,
   215,
   217,
   218,
   220,
   221,
   222,
   223,
   225,
   226,
   227,
   228,
   233,
   234,
   236,
   237,
   238,
   239,
   240,
   241,
   242,
   243,
   245,
   247,
   249,
   251,
   252,
   253,
   255,
   256,
   334,
   258,
   259,
   260,
   263,
   265,
   266,
   268,
   269,
   270,
   271,
   272,
   274,
   275,
   276,
   277,
   335,
   280,
   282,
   283,
   333,
   286,
   287,
   288,
   289,
   291,
   292,
   293,
   329,
   330,
   295,
   297,
   332,
   299,
   300,
   301,
   303,
   305,
   306,
   331,
   326,
   307,
   308,
   312,
   313,
   314,
   315,
   316,
   321,
   324,
   325,
]

PRODUCT_CATEGORIES = [
   1,
   8,
   537,
   111,
   141,
   166,
   222,
   412,
   436,
   632,
   469,
   536,
   5181,
   772,
   783,
   922,
   5605,
   2092,
   988,
   1239,
   888,
]

SECTORS_WITH_LABELS = {

   "SECURITY": "Security",
   "SOFTWARE_AND_COMPUTER_SERVICES": "Software and computer services",
   "TEXTILES_INTERIOR_TEXTILES_AND_CARPETS": "Textiles, interior textiles and carpets",
   "WATER": "Water",
}



SECTORS = [
   "AEROSPACE",
   "ADVANCED_MANUFACTURING",
   "AIRPORTS",
   "AGRICULTURE_HORTICULTURE_AND_FISHERIES",
   "AUTOMOTIVE",

   "WATER",
]

# these user credentials are hard-coded in `directory-sso`. The users
# are created when `manage.py create_test_users` is ran on sso.
USERS = {
    "verified": {
        "username": env.str("SSO_USER_USERNAME"),
        "password": env.str("SSO_USER_PASSWORD"),
        "token": env.str("SSO_USER_TOKEN"),
        "sso_id": env.int("SSO_USER_SSO_ID"),
    },
    "unverified": {"token": env.str("SSO_UNVERIFIED_USER_TOKEN")},
}

LOAD_TESTS_USER_AGENT = {"User-Agent": "locust - load tests"}
