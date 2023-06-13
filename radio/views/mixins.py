from typing import Any

from django.db.models import QuerySet, Q


class SearchMixin:
    search_fileds: list[str] = []
    search_name: str = 'search'

    def get_serch_value(self) -> str:
        return self.request.GET.get(self.search_name)

    def get_queryset(self) -> QuerySet[Any]:
        if hasattr(super(), 'get_queryset'):
            queryset = super().get_queryset()

            print("searching")

            search_value = self.get_serch_value()

            if not search_value:
                return queryset

            fr = [{v: search_value} for v in self.search_fileds]

            f = Q()
            for field in fr:
                f = f.__or__(Q(**field))

            return queryset.filter(f)
