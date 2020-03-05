import json

from django.db    import IntegrityError
from django.views import View
from django.db.models import Count
from django.http  import HttpResponse, JsonResponse

from products.models import Product, Recipe, Bundle

class HomeView(View):
    def get(self, request):
        product_data_caching = Product.objects.prefetch_related('category').select_related('season', 'harvest_year', 'measure')
        bundle_data_caching  = Bundle.objects.prefetch_related('product_set')
        bundle_info          = bundle_data_caching.values('title', 'price')
        content_info         = [
                list(data.product_set.values('measure_id__measure', 'name')
                    .annotate(Count('name'))) for data in bundle_data_caching
                ]
        bundle_deal          = [data for data in zip(bundle_info, content_info)]        
        category_deal        = product_data_caching.filter(is_main=True, discount_rate='', category__name='fresh').values(
                'id',
                'name', 
                'category__name', 
                'big_image2'
        )
        seasonal_deal        = product_data_caching.filter(is_main=True, season_id__name='september').values(
                'id',
                'discount_rate', 
                'name', 
                'season_id__name', 
                'big_image1'
        )
        recommand_product    = product_data_caching.all().order_by('id').filter(is_main = True).exclude(is_in_stock=0, big_image1='').values(
                'id',
                'price',
                'name',
                'small_image',
                'big_image1',
                'big_image2',
                'big_image3',
                'harvest_year_id__year',
                'measure_id__measure',
                'is_on_sale',
                'is_in_stock',
        )
        return JsonResponse(
                {'data' : 
            {
                'category_deal'     : list(category_deal), 
                'seasonal_deal'     : list(seasonal_deal), 
                'recommand_product' : list(recommand_product),
                'bundle_deal'       : list(bundle_deal),
                }
            }, status = 200)
