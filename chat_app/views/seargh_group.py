
from django.views.generic import ListView
from django.db.models import Q

from chat_app.models import ChatGroupsName


class UserSearchListView(ListView):
    """View поиска пользователей"""

    model = ChatGroupsName
    queryset = ChatGroupsName.objects.all()
    template_name = "chat_app/search.html"
    context_object_name = "searchlists"

    def get_queryset(self):
        # Получаем не отфильтрованный кверисет всех моделей
        queryset = super(UserSearchListView, self).get_queryset()
        q = self.request.GET.get("q")

        if q:
            # Если 'q' в GET запросе, фильтруем кверисет по данным из 'q'
            # Для поиска пользователей у которых есть такое в имени.

            return queryset.filter(Q(title__icontains=q))
            # Для поиска пользователей у которых начинается имя c q.
            # return queryset.filter(Q(title__startswith=q))
        return None