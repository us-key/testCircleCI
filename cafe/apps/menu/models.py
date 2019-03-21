from django.db import models

# Create your models here.
TEA_KINDS = (
    ("english", "英国紅茶"),
    ("chinese", "中国茶"),
    ("japanese", "日本茶"),
)

class TeaManager(models.Manager):
    def count_each_kind(self):
        """お茶の種類別件数を辞書で返します。"""
        result = self.values_list("kind").annotate(
            count=models.Count("kind")
        )
        return dict(result)

class Tea(models.Model):
    objects = TeaManager()

    name = models.CharField("名称", max_length=255)
    kind = models.CharField("種類", max_length=255, choices=TEA_KINDS)