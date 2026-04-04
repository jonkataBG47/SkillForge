from django.db import migrations


MANAGER_GROUP_NAME = "Content Managers"
VIEWER_GROUP_NAME = "Content Viewers"


def create_groups_with_permissions(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")

    manager_group, _ = Group.objects.get_or_create(name=MANAGER_GROUP_NAME)
    viewer_group, _ = Group.objects.get_or_create(name=VIEWER_GROUP_NAME)

    manager_permission_codenames = [
        "add_category",
        "change_category",
        "delete_category",
        "view_category",
        "add_skill",
        "change_skill",
        "delete_skill",
        "view_skill",
        "add_resource",
        "change_resource",
        "delete_resource",
        "view_resource",
        "add_learningpath",
        "change_learningpath",
        "delete_learningpath",
        "view_learningpath",
        "view_skillforgeuser",
    ]

    viewer_permission_codenames = [
        "view_category",
        "view_skill",
        "view_resource",
        "view_learningpath",
        "view_skillforgeuser",
    ]

    manager_permissions = Permission.objects.filter(
        codename__in=manager_permission_codenames
    )
    viewer_permissions = Permission.objects.filter(
        codename__in=viewer_permission_codenames
    )

    manager_group.permissions.set(manager_permissions)
    viewer_group.permissions.set(viewer_permissions)


def delete_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(
        name__in=[MANAGER_GROUP_NAME, VIEWER_GROUP_NAME]
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0007_alter_skillforgeuser_email"),
        ("category", "0005_alter_category_name"),
        ("skills", "0015_alter_skill_title"),
        ("resources", "0009_alter_resource_title"),
        ("learning_paths", "0003_alter_learningpath_title"),
    ]

    operations = [
        migrations.RunPython(create_groups_with_permissions, delete_groups),
    ]
