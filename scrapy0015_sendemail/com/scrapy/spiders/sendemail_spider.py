"""
注意:twisted.mail.smtp还不支持python3，
所以可以采取别发邮件的组件:smtplib
目前
class scrapy.mail.MailSender(smtphost=None, mailfrom=None, smtpuser=None, smtppass=None, smtpport=None)
    参数:    
        smtphost (str) – 发送email的SMTP主机(host)。如果忽略，则使用 MAIL_HOST 。
        mailfrom (str) – 用于发送email的地址(address)(填入 From:) 。 如果忽略，则使用 MAIL_FROM 。
        smtpuser – SMTP用户。如果忽略,则使用 MAIL_USER 。 如果未给定，则将不会进行SMTP认证(authentication)。
        smtppass (str) – SMTP认证的密码
        smtpport (int) – SMTP连接的短裤
        smtptls – 强制使用STARTTLS
        smtpssl (boolean) – 强制使用SSL连接
    classmethod from_settings(settings)
        使用Scrapy设置对象来初始化对象。其会参考 这些Scrapy设置.
        参数:    settings (scrapy.settings.Settings object) – the e-mail recipients
    send(to, subject, body, cc=None, attachs=(), mimetype='text/plain')
        发送email到给定的接收者。
        参数:    
            to (list) – email接收者
            subject (str) – email内容
            cc (list) – 抄送的人
            body (str) – email的内容
            attachs (iterable) – 可迭代的元组 (attach_name, mimetype, file_object)。 attach_name 是一个在email的附件中显示的名字的字符串， mimetype 是附件的mime类型， file_object 是包含附件内容的可读的文件对象。
            mimetype (str) – email的mime类型
Mail设置
这些设置定义了 MailSender 构造器的默认值。其使得在您不编写任何一行代码的情况下，为您的项目配置实现email通知的功能。
MAIL_FROM
默认值: 'scrapy@localhost'
用于发送email的地址(address)(填入 From:) 。
MAIL_HOST
默认值: 'localhost'
发送email的SMTP主机(host)。
MAIL_PORT
默认值: 25
发用邮件的SMTP端口。
MAIL_USER
默认值: None
SMTP用户。如果未给定，则将不会进行SMTP认证(authentication)。
MAIL_PASS
默认值: None
用于SMTP认证，与 MAIL_USER 配套的密码。
MAIL_TLS
默认值: False
强制使用STARTTLS。STARTTLS能使得在已经存在的不安全连接上，通过使用SSL/TLS来实现安全连接。
MAIL_SSL
强制使用SSL加密连接。
"""
from scrapy.mail import MailSender
class SendMail():
    mailer = MailSender()
    #可以从系统变量设置中获取发送信息
    #mailer = MailSender.from_settings(settings)
    #自己也可以创建一个
    mailer = MailSender()
    mailer.smtphost='smtp.126.com'
    mailer.mailfrom='zhangkunjie'
    mailer.smtpuser="zhangkunjie1988@126.com"
    mailer.smtppass="PPxy168891"
    mailer.smtpport=25
    mailer.send(to=["907535517@qq.com"], subject="Some subject", body="Some body", cc=["zhangkunjie1988@126.com"])