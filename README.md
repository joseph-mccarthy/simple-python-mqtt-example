# Simple Python MQTT Example

I'm starting to use Raspberry Pi for a lot of simple tasks around the home and give me notfications. So I thought it was about time to look into message brokers and __MQTT__ is the way to go. So instead of just throwing the implmentation into a project of mine. I thought it would be more useful to create a seriously simple example project that just publishes a random number to a topic and another that subscribes to it. The two files __publish.py__ and __subscribe.py__ are both heavily commented with what basically each line is doing. So it's simple to follow.

## Brokers

In order to publish and subscribe to messages you'll require a broker. [__HiveMQ__](http://www.mqtt-dashboard.com/) has a free open MQTT broker that you could use. If you are going to use HiveMQ free public broker __please remember that it's public and don't share sensitive information__. I'm personally using [__Mosquitto__](https://github.com/eclipse/mosquitto) as my broker on the network, running on a Raspberry Pi (Obviously).

### Installing Mosquitto (Raspberry Pi)

Mosquitto is already avaliable in the standard distribution so it's just a case of:

```bash
sudo apt-get install mosquitto
```

This will default to always be running using port __1883__. That's all the set up that I needed to get this demo working, although the [__documentation__](https://mosquitto.org/documentation/) is great for Mosquitto. Note that this will also only allow for localhost connections. If you want to allow for remote connections then do the following:

```bash
sudo nano /etc/mosquitto/mosquitto.conf
```

Then add the following two lines at the bottom of the file

```bash
listner 1883
allow_anonymous true
```

Note that this is not a secure implmentation and should not be used in production.


## Licence

MIT License

Copyright (c) 2022 Joseph McCarthy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Author Info

- [GitHub](https://github.com/joseph-mccarthy)
- [Website](https://joseph-mccarthy.github.io/)