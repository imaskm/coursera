# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    MAX_SIZE = 0
    TIME_REACHED = 0

    def __init__(self, size):
        self.size = size
        self.finish_time = 0
        self.queue       = []

    def process(self, request):
        # write your code here
        Buffer.TIME_REACHED += request.arrived_at
        if(self.size < 1 ):
            return Response( True, -1)
        
        if(self.queue == [] ):
            self.size-=1
            self.finish_time= (request.arrived_at+request.time_to_process )
            self.queue.append(request)
            return Response(False,request.arrived_at)
        else:
            c = 0
            for req in self.queue:
                
                if( req.arrived_at + req.time_to_process + c <= Buffer.TIME_REACHED  ):
                    c = req.arrived_at + req.time_to_process
                    self.queue.pop(0)

            if(self.finish_time  > request.arrived_at ):
                self.finish_time-=request.arrived_at
                self.queue.append(request)
            else:
                self.queue.pop(0)


            

        return Response(False, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
