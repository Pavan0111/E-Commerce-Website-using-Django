
from django.urls import path
from.import views
urlpatterns = [
    path ("", views.index, name="ShopeHome"),
    path ("about/", views.about, name="AboutUs"),
    path ("contact/", views.contact, name="ContactUs"),
    path ("tracker/", views.tracker, name="TrackingStatus"),
    path ("productView/", views.productView, name="productView"),
    path ("checkout/", views.checkout, name="Checkout"),

]
