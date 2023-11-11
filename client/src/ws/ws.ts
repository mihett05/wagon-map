import { v4 } from 'uuid';

export class Response {
  constructor(
    public readonly event: string,
    public readonly uid: string,
  ) {}
}

type ResolveArg = {
  response: Response;
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  data: any;
};

type Resolve = (arg: ResolveArg) => void;

export class Ws {
  private resolves: { [uid: string]: [Resolve, (reason: string) => void] };

  constructor(private readonly socket: WebSocket) {
    this.resolves = {};
    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.uid === undefined) {
        throw new TypeError("Server didn't return 'uid'");
      }
      this.resolves[data.uid][0]({
        response: new Response(data.event, data.uid),
        data,
      });
    };
  }

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  public async send(event: string, data: any): Promise<ResolveArg> {
    const request = {
      event,
      uid: v4(),
      ...data,
    };
    this.socket.send(JSON.stringify(request));
    return new Promise((resolve, reject) => {
      this.resolves[request.uid] = [resolve, reject];
    });
  }

  public close() {
    this.socket.close();
    Object.keys(this.resolves).forEach((key: keyof typeof this.resolves) => {
      this.resolves[key][1]('Connection is closed');
    });
  }
}
