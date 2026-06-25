from django.core.management.base import BaseCommand
from investments.models import Investment


class Command(BaseCommand):

    help = "Distribute daily profit"

    def handle(self, *args, **kwargs):

        investments = Investment.objects.filter(
            active=True
        )

        for investment in investments:

            package = investment.package
            user = investment.user

            user.wallet_balance += package.daily_profit
            user.save()

            investment.total_profit += package.daily_profit
            investment.days_completed += 1

            if investment.days_completed >= package.duration_days:
                investment.active = False

            investment.save()

        self.stdout.write(
            self.style.SUCCESS(
                "Daily profit distributed successfully."
            )
        )