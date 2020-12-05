# Generated by Django 2.2.12 on 2020-11-14 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stddata', '0003_script'),
        ('gcd', '0033_add_characters'),
        ('oi', '0031_housekeeping'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupRevision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('committed', models.NullBooleanField(db_index=True, default=None)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('sort_name', models.CharField(default='', max_length=255)),
                ('disambiguation', models.CharField(blank=True, db_index=True, max_length=255)),
                ('year_first_published', models.IntegerField(blank=True, db_index=True, null=True)),
                ('year_first_published_uncertain', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('keywords', models.TextField(blank=True, default='')),
                ('changeset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grouprevisions', to='oi.Changeset')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revisions', to='gcd.Group')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stddata.Language')),
                ('previous_revision', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_revision', to='oi.GroupRevision')),
            ],
            options={
                'db_table': 'oi_group_revision',
                'ordering': ['created', '-id'],
            },
        ),
        migrations.CreateModel(
            name='GroupMembershipRevision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('committed', models.NullBooleanField(db_index=True, default=None)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('organization_name', models.CharField(max_length=200)),
                ('year_joined', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('year_joined_uncertain', models.BooleanField(default=False)),
                ('year_left', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('year_left_uncertain', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
                ('changeset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groupmembershiprevisions', to='oi.Changeset')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership_revisions', to='gcd.Character')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership_revisions', to='gcd.Group')),
                ('group_membership', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revisions', to='gcd.GroupMembership')),
                ('membership_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gcd.GroupMembershipType')),
                ('previous_revision', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_revision', to='oi.GroupMembershipRevision')),
            ],
            options={
                'verbose_name_plural': 'Character Group Membership Revisions',
                'db_table': 'oi_group_membership_revision',
                'ordering': ['created', '-id'],
            },
        ),
        migrations.CreateModel(
            name='CharacterRevision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('committed', models.NullBooleanField(db_index=True, default=None)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('sort_name', models.CharField(default='', max_length=255)),
                ('disambiguation', models.CharField(blank=True, db_index=True, max_length=255)),
                ('year_first_published', models.IntegerField(blank=True, db_index=True, null=True)),
                ('year_first_published_uncertain', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('keywords', models.TextField(blank=True, default='')),
                ('changeset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characterrevisions', to='oi.Changeset')),
                ('character', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revisions', to='gcd.Character')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stddata.Language')),
                ('previous_revision', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_revision', to='oi.CharacterRevision')),
            ],
            options={
                'db_table': 'oi_character_revision',
                'ordering': ['created', '-id'],
            },
        ),
        migrations.CreateModel(
            name='CharacterRelationRevision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('committed', models.NullBooleanField(db_index=True, default=None)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('notes', models.TextField(blank=True)),
                ('changeset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characterrelationrevisions', to='oi.Changeset')),
                ('character_relation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revisions', to='gcd.CharacterRelation')),
                ('from_character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_character_revisions', to='gcd.Character')),
                ('previous_revision', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_revision', to='oi.CharacterRelationRevision')),
                ('relation_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revisions', to='gcd.CharacterRelationType')),
                ('to_character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_character_revisions', to='gcd.Character')),
            ],
            options={
                'verbose_name_plural': 'Character Relation Revisions',
                'db_table': 'oi_character_relation_revision',
                'ordering': ('to_character', 'relation_type', 'from_character'),
            },
        ),
        migrations.CreateModel(
            name='CharacterNameDetailRevision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('committed', models.NullBooleanField(db_index=True, default=None)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('sort_name', models.CharField(default='', max_length=255)),
                ('changeset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characternamedetailrevisions', to='oi.Changeset')),
                ('character', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='name_revisions', to='gcd.Character')),
                ('character_name_detail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revisions', to='gcd.CharacterNameDetail')),
                ('character_revision', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='character_name_revisions', to='oi.CharacterRevision')),
                ('previous_revision', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_revision', to='oi.CharacterNameDetailRevision')),
            ],
            options={
                'verbose_name_plural': 'Character Name Detail Revisions',
                'db_table': 'oi_character_name_detail_revision',
                'ordering': ['sort_name'],
            },
        ),
    ]
