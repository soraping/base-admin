from django.shortcuts import render
from django.views.generic.base import View

from .models import Wxa_o2o


# Create your views here.

class O2OUserListView(View):

    def get(self, request):

        query_params = request.GET

        # 页码
        page_no = int(query_params.get('page_no', 1))
        limit = 10
        offset = (page_no - 1) * limit
        """
        skip 跳过 (page - 1) * limit 后的 limit(条数据)
        设 page_no = 3 
        limit = (page_no - 1) * 10
        则 offset = 20 ，即，跳过前20条数据，从21条开始数，取10条
        """
        o2o_list: list[Wxa_o2o] = Wxa_o2o.objects().skip(offset).limit(limit)
        count = o2o_list.count()

        return render(request, 'index.html', {
            'o2o_list': o2o_list,
            'count': count
        })
