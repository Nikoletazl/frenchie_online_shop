from django.views.generic import TemplateView

from frenchie_online_shop.web.models import Product, Album


class StoreView(TemplateView):
    model = Product
    template_name = 'store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = list(Product.objects.all())

        context.update(
            {
                'products': products,
            }
        )

        return context


class HomePageView(TemplateView):
    model = Album
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = list(Album.objects.all())

        context.update(
            {
                'photos': photos,
            }
        )

        return context
