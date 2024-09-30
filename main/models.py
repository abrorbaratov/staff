from django.db import models
from django.core.exceptions import ValidationError


class Department(models.Model):
    name = models.CharField(max_length=255)
    parent_department = models.ForeignKey(
        "self",
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name="sub_departments",
    )

    def check_for_depth(self):
        depth = 0
        parent = self.parent_department
        while parent:
            parent = parent.parent_department
            depth += 1
        if depth >= 5:
            raise ValidationError("Maximum department hierarchy depth can be five!")

    def save(self, *args, **kwargs):
        self.check_for_depth()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class JobTitle(models.Model):
    title = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.title


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    employment_date = models.DateField()
    salary = models.PositiveBigIntegerField()
    job_title = models.ForeignKey(JobTitle, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["-id"]
