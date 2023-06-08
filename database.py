from sqlalchemy import create_engine, text

engine = create_engine(
 "mysql+pymysql://as608lgwzmzbczfvjykt:pscale_pw_HIsPwBMPi0Xkji8zjYMk2ziJbWWK63Z6Oiar4AkE82R@aws.connect.psdb.cloud/datauploadarvind?charset=utf8mb4",
 connect_args={
	 "ssl": {
  		"ssl_ca": "/etc/ssl/cert.pem"
 }
})
with engine.connect() as conn:
	result = conn.execute(text("select * from jobs"))
	print(result.all())
