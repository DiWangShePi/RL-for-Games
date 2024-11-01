# Liar's Bar

> 骗子酒吧，steam链接：https://store.steampowered.com/app/3097560/Liars_Bar/?l=schinese&curator_clanid=28673811

虽然是针对这一游戏的AI，但这一实现不考虑将代码直接接入游戏。这一部分的内容更偏向于游戏工程而非AI，因此我希望将游戏的内容抽象出来。

###### 游戏规则 -- Liar's Deck

牌桌上共有20张牌：6张A，6张K，6张Q，大王小王各一张。每一局游戏共有四名玩家，轮流出牌。每名玩家初始手牌均为五张。

游戏开始时在A，K，Q中随机选择一个，玩家在这一回合中只能打出该牌(假设为A)。打牌的方式为打出指定数量的纸牌(由玩家选择，一张到三张。假设为两张)，背面朝上放入弃牌堆中。这代表玩家(假设为bob)做出声明：我打出了两张A。该玩家的下一位(假设为alice)可以选择承认该声明或否认该声明。承认则由alice出牌，否认则将bob打出的牌进行检验。如果存在至少一张不为A的，则bob受到惩罚，否则alice受到惩罚。

每一局游戏中，第一位出牌的玩家不能进行否认。若三位玩家均出完了手中的牌，则最后一名玩家必须对上一名玩家的结果进行否认。

我们注意到，由于每一轮选中的牌只有八张(大小王算作任意牌)，玩家获得五张选中的牌的概率为$C_8^5 / C_{20}^5 = 56 / 15504 \approx 0.004$。因此，绝大部分情况下，玩家想要出完手中的牌，就必须撒谎。

###### 环境构建

我们首先注意到，A，K，Q和大小王的设定是为了增添游戏的趣味性。实际上每一轮中，玩家遇到的牌只有两类：指定牌型和非指定牌型。

因此我们可以用0和1代替这些信息。初始时，环境存在八个0和十二个1，agent从中随机的获取到5个数字，代表拿到的牌。限定指定牌型为0，即agent必须要打出0。

接下来，agent每一回合进行的动作可以被分为三种。

- 0：对上一名agent的出牌进行否认
- 1：诚实出牌。接收参数n，代表打出的0的数量。
- 2：欺诈出牌。接收参数n，代表打出的1的数量。

更加完备的实现是将1和2两种动作均表示为出牌，随后agent再进一步选择几张0或者1。但在这一阶段的实现中，我们认为混杂0和1的出牌是没有道理的，因而将出牌的行为简单的划归两类。因为这不会让agent在受到挑战时被判定为诚实，且会降低手中的诚实牌的数量。



