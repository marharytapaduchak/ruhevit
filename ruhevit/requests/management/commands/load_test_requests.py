import random
from django.core.management.base import BaseCommand
from accounts.models import User
from requests.models import Request, RequestHistory


class Command(BaseCommand):
    help = "Generate test data: requests and request history"

    def handle(self, *args, **kwargs):
        TYPES = ['medicine', 'ammo', 'drones', 'transport', 'repair']
        PRIORITIES = ['high', 'medium', 'low']
        LOCATIONS = ['front', 'near_rear', 'far_rear']
        STATUSES = ['need_volunteer', 'in_progress',
                    'pending', 'done', 'rejected']

        military_users = list(User.objects.filter(role='військовий'))
        volunteers = list(User.objects.filter(role='волонтер'))

        if not military_users:
            self.stdout.write(self.style.ERROR("❌ No military users found"))
            return

        self.stdout.write("🛠️ Creating test requests...")

        requests = []
        for i in range(1, 21):
            owner = random.choice(military_users)
            executor = random.choice(
                volunteers) if volunteers and random.random() < 0.7 else None

            req = Request.objects.create(
                owner=owner,
                executor=executor,
                name=f"Test Request #{i}",
                description="Автоматично згенерований тестовий запит",
                type=random.choice(TYPES),
                priority=random.choice(PRIORITIES),
                location=random.choice(LOCATIONS),
                status=random.choice(STATUSES)
            )
            requests.append(req)

        self.stdout.write(self.style.SUCCESS(
            f"✅ Created {len(requests)} requests."))

        self.stdout.write("📜 Creating request history...")

        history_count = 0
        for req in requests:
            entries = random.randint(2, 4)
            used_statuses = random.sample(STATUSES, entries)
            for status in used_statuses:
                RequestHistory.objects.create(request=req, status=status)
                history_count += 1

        self.stdout.write(self.style.SUCCESS(
            f"✅ Created {history_count} history entries."))
