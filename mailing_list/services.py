from django.core.mail import send_mail
from datetime import datetime, timezone
from config import settings
from mailing_list.models import MESSAGE, SETTINGS, ATTEMPT
from crontab import CronTab
from datetime import datetime, timedelta


def send_order_email(obj: SETTINGS):
    try:

        send_mail(
            obj.message.letter_subject,
            obj.message.letter_body,
            settings.EMAIL_HOST_USER,
            [*obj.clients.all()],
            fail_silently=True)

        mail_attempt = ATTEMPT.objects.create(  # запись в таблицу ATTEMPT об успешности выполнения
            settings=obj,
            message=obj.message.letter_subject,
            date=datetime.now(),
            status=True,
            server_answer='Mail delivered successfully'

        )
    except Exception as e:

        mail_attempt = ATTEMPT.objects.create( # запись в таблицу ATTEMPT об ошибке
            settings=obj,
            message=obj.message.letter_subject,
            date=datetime.now(),
            status=False,
            server_answer=str(e)

        )


def time_task():
    current_date = datetime.now().date()  # получение текущей даты

    mailings_created = SETTINGS.objects.filter(
        status='CREATED')  # выборка из базы данных всех рассылок со статусом создана

    if mailings_created.exists():  # проверка пустой ли список или нет

        for mailing in mailings_created:

            if mailing.start_time <= current_date <= mailing.end_time:  # проверка пришло ли время рассылки

                mailing.status = 'LAUNCHED'
                mailing.save()

    mailings_launched = SETTINGS.objects.filter(
        status='LAUNCHED')  # выборка из базы данных всех рассылок со статусом запущено

    if mailings_launched.exists():  # проверка пустой ли список или нет

        for mailing in mailings_launched:

            if mailing.start_time <= current_date <= mailing.end_time:  # проверка находится ли текущая дата внутри промежутка времени между началом и концом рассылки
                if mailing.last_run:  # если до текущего момента уже был запуск рассылки

                    differance = current_date - mailing.last_run  # разница между текущей датой и последним запуском

                    if mailing.frequency == 'daily':

                        if differance.days == 1:  # если разница между текущей датой и последней датой запуска равна 1 дню
                            send_order_email(mailing)  # запуск рассылки
                            mailing.last_run = current_date  # установление новой даты последнего запуска

                            mailing.save()

                    elif mailing.frequency == 'weekly':

                        if differance.days == 7:  # если разница между текущей датой и последней датой запуска равна 7 дням
                            send_order_email(mailing)  # запуск рассылки
                            mailing.last_run = current_date  # установление новой даты последнего запуска

                            mailing.save()

                    elif mailing.frequency == 'monthly':

                        if differance.days == 30:  # если разница между текущей датой и последней датой запуска равна 30 дням
                            send_order_email(mailing)  # запуск рассылки
                            mailing.last_run = current_date  # установление новой даты последнего запуска

                            mailing.save()





                else:  # если расслыка ещё не запускалась
                    send_order_email(mailing)  # запуск рассылки
                    mailing.last_run = current_date  # установление новой даты последнего запуска
                    mailing.save()

            elif current_date >= mailing.end_time:  # если текущая дата больше чем конец рассылки

                mailing.status = 'COMPLETED'

                mailing.save()
