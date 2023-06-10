import json
import logging
import shutil
from typing import Any

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from radio.models import Radio


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Добавить в базу список радио станций'

    def handle(self, *args: Any, **options: Any) -> str | None:
        logger.info("Старт заполнения базы...")
        try:
            with open(settings.BASE_DIR / 'radio_src/list.json',
                      mode='r') as file:

                station_list = json.loads(file.read())

                for raw_radio in station_list:
                    created_station = Radio.objects.get_or_create(**raw_radio)

                    print("Создание модели: ", created_station)

            shutil.copytree(settings.BASE_DIR / 'radio_src/previews',
                            settings.MEDIA_ROOT / 'previews',
                            dirs_exist_ok=True)

        except FileNotFoundError as err:
            raise CommandError("Файл не найден", err.filename)
