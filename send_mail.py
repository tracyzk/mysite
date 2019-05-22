import os
# from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    subject, from_email, to = '来自www.标题.com的测试邮件', 'zhangbintest@lianluo.com', '517188538@qq.com'
    text_content = 'new欢迎访问www.内容.com，这里是刘江的博客和教程站点，专注于Python和Django技术的分享！'
    html_content = 'new1<p>欢迎访问<a href="http://www.liujiangblog.com" target=blank>www.liujiangblog.com</a>，这里是刘江的博客和教程站点，本站专注于Python、Django和机器学习技术的分享！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
'''
if __name__ == '__main__':

    send_mail(
        '来自www.主题.com的测试邮件',
        '欢迎访问www.内容.com，这里是刘江的博客和教程站点，本站专注于Python、Django和机器学习技术的分享！',
        'zhangbintest@lianluo.com',
        ['517188538@qq.com'],
    )
'''
