from Controller.auto_time_tracker import auto_time_tracker
from Service.requisicoes import ClockifyClient


if __name__ == '__main__':
   cliente = ClockifyClient()
   auto_time_tracker(cliente)