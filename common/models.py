from django.db import models
from django.utils.timezone import localtime


class DefaultTimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일시")
    modified_at = models.DateTimeField(auto_now=True, verbose_name="변경일시")

    class Meta:
        abstract = True


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(
        default=False, blank=True, null=True, verbose_name="삭제여부"
    )
    deleted_at = models.DateTimeField(
        default=None, blank=True, null=True, verbose_name="삭제일시"
    )

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted = localtime()
        self.save(update_fields=["is_deleted", "deleted_at"])
