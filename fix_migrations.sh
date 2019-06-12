echo -e "\n    WARNING: Did you backup your database?\n"
read -p '    Type "yes" to proceed: ' confirmation

if [[ "$confirmation" == "yes" ]]; then

    echo -e -n "\n    Press Ctrl+C to cancel... Counting down: "
    read -t 1 -n 1 -s -r -p "5..."
    read -t 1 -n 1 -s -r -p "4..."
    read -t 1 -n 1 -s -r -p "3..."
    read -t 1 -n 1 -s -r -p "2..."
    read -t 1 -n 1 -s -r -p "1..."
    echo -e "\n    Fixing migrations\n"

    echo "DELETE FROM django_migrations" | python manage.py dbshell

    python manage.py migrate contenttypes 0001_initial --fake
    python manage.py migrate auth 0001_initial --fake 2> /dev/null
    python manage.py migrate contenttypes 0002_remove_content_type_name --fake 2> /dev/null
    python manage.py migrate auth 0002_alter_permission_name_max_length --fake
    python manage.py migrate auth 0003_alter_user_email_max_length --fake
    python manage.py migrate auth 0004_alter_user_username_opts --fake
    python manage.py migrate auth 0005_alter_user_last_login_null --fake
    python manage.py migrate auth 0006_require_contenttypes_0002 --fake
    python manage.py migrate auth 0007_alter_validators_add_error_messages --fake
    python manage.py migrate auth 0008_alter_user_username_max_length --fake
    python manage.py migrate sessions 0001_initial --fake
    python manage.py migrate auth 0009_alter_user_last_name_max_length --fake
    python manage.py migrate admin 0001_initial --fake
    python manage.py migrate admin 0002_logentry_remove_auto_add --fake
    python manage.py migrate admin 0003_logentry_add_action_flag_choices --fake

    python manage.py migrate user 0001_initial --fake
    python manage.py migrate user 0002_user_updated_at

    python manage.py migrate entry 0001_initial --fake
    python manage.py migrate entry 0002_auto_20190320_1903 --fake
    python manage.py migrate entry 0003_post_title --fake
    python manage.py migrate entry 0004_auto_20190320_1910 --fake
    python manage.py migrate entry 0005_post_is_published --fake
    python manage.py migrate entry 0006_post_trailing_html --fake
    python manage.py migrate entry 0007_post_slug --fake
    python manage.py migrate entry 0008_remove_post_trailing_html --fake


else
    echo -e "\n    Aborting...\n"
fi
