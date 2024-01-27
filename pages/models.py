from django.db import models
from django.utils.translation import gettext_lazy as _


# ------------------------ Home ------------------------ #

# ------ Home.GalleryModel ------ #
class GalleryModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("name"))
    photo = models.ImageField(verbose_name=_("photo"))
    ingredient = models.CharField(max_length=460, verbose_name=_("ingredient"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("gallery")
        verbose_name_plural = _("galleries")

# ------------------------ Blog and Home ------------------------ #

# ------ Home and Blog.NewsModel ------ #
class NewsModel(models.Model):
    photo = models.ImageField(upload_to='images', verbose_name=_("photo"))
    title = models.CharField(max_length=400, verbose_name=_("title"))
    description = models.TextField(verbose_name=_("description"))

    created_at = models.DateField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("updated_at"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("new")
        verbose_name_plural = _("news")


# ------------------------ About ------------------------ #

# ------ Home.WorkerModel ------ #
class WorkerModel(models.Model):
    full_name = models.CharField(max_length=200, verbose_name=_("full_name"))
    photo = models.ImageField(upload_to='images', verbose_name=_("photo"))
    description = models.TextField(verbose_name=_("description"))

    created_at = models.DateField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    def __str__(self):
        return f"{self.full_name}, {self.created_at}"

    class Meta:
        verbose_name = _("worker")
        verbose_name_plural = _("workers")


# ------ Home.CategoryModel ------ #
class CategoryModel(models.Model):
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")


# ------ Home.ProductModel ------ #
class ProductModel(models.Model):
    photo = models.ImageField(verbose_name=_("photo"))
    title = models.CharField(max_length=255, verbose_name=_("title"))
    price = models.FloatField(verbose_name=_("price"))
    description = models.CharField(max_length=255, verbose_name=_("description"))
    in_stock = models.BooleanField(default=True, verbose_name=_("in_stock"))

    categories = models.ManyToManyField(CategoryModel, related_name="products")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
