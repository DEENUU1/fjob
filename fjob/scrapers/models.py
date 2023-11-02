from django.db import models


class PageContent(models.Model):
    content = models.TextField()
    content_json = models.JSONField(default=None, blank=True, null=True)
    website = models.CharField(max_length=100)
    is_parsed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.website} - {self.is_parsed} - {self.date_created}"

    class Meta:
        ordering = ["-date_created"]
        verbose_name = "Page Content"
        verbose_name_plural = "Page Contents"
