# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://aws_rkari:newpassword@flasktest.cryxwnwcbmqt.us-west-1.rds.amazonaws.com:3306/flasktestdb'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://aws_rkari:newpassword@https://584126383582.signin.aws.amazon.com/console:3306/flasktestdb'

# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'L2gkGvpyezc3EqrbJNGYY3B4Ew+mVK6x+a69PTnU'
