# Odds, Result Estimate, and Return Rate in The Sports Bet

## Odds

"Odds" is the most primary and basic concept in sports bet. We take the "decimal odds" (used in Europe) for an example. The bookmaker announce the ratio of full payout to the stake for each game result. Given a game with "host A v.s. guest B", if the announced odds are ow, od, and ol, it means

- if you placed wager w on "host A wins", then you will get w * ow when A finally wins;
- if you placed wager w on "draw game", then you will get w * od when the final result is draw;
- if you placed wager w on "host A loses", then you will get w * ol when A finally loses.

Thus you can see the decimal odds should be no less than 1.0 in usual case. How does the bookmaker get these odds numbers? People usuauly tell you the bookmaker hired a lot of analyzers and make their estimate about the game result, which leads to the announced odds. Well, this is not a wrong answer. However, it's not correct neither. To understand the odds, the first thing you should know is "fair bet", in which the bookmaker is not one of the betters. In such case, the most important resources for the bookmaker to get the proper odds are the wagers they received, and the "return rate".

## Return Rate

The basic way for the bookmakers to earn their benefit is to take the "up-front" from the wagers paid by the bettors (think it as "service fees"). This leads to another important concept in bet - the "return rate".

With all the wagers placed, say m in total, the bookmaker only take part of the total amount, say w, as the "prize" for the winners. Then the remaining is kept as the bookmaker's profit, or called as "up-front". The proportion of w in m, is defined as the "return rate".

    return rate = winner prize / total wager

Now we can continue talk about how the odds are calculated. In the total wager w, let's say there are ww among the total amount for "host A wins", wd for "draw game", and wl for "host A loses". Since the bookmaker always pay m (w * return rate ) as the winner prize. Then the decimal odds are as follows

- odds for "host A wins" : w * return rate / ww;
- odds for "draw game" : w * return rate / wd;
- odds for "host A loses" : w * return rate / wl.

## Result Estimate

So far so good. If you pay attention to any website publishing the odds information, posssibly you will see three numbers in percentage called "winning probability", "draw probability" and "losing probability". These numbers are just another interpratation about the odds (as well as "return rate", which is often provided by the website to save the bettors' effort). Then the question is, how are these probabilities calculated?

Here is an explaination about the calculation of the "winning/draw/losing probabilities" based on the following assumption: with total wager w and a preferred return rate r, the bookmaker annouces the odds with which the expectation of payout is w * r.

Given this assumption, now we consider how the bookmaker choose the oods. Recall that ow, od, and ol are the odds for "winning", "draw", and "losing". Let pw, pd, and pl be the probabilities for "winning", "draw" and "losing". Then the payout expectation is

    return expectation = pw * ww * ow + pd * wd * od + pl * wl * ol = w * r

The most direct way to make this always true is to let

    pw * ow = r
    pd * od = r
    pl * ol = r

Note that r can also be derived from the announced odds. As we mentioned, the bookmaker calculate the odds to make sure for any game result, the payout is w * r. That is

    ow * ww = w * r
    od * wd = w * r
    ol * wl = w * r

Since w = ww + wd + wl, we have

    r = 1 / (1 / ow + 1 / od + 1/ ol)

Thus we know the bookmaker's estimate about probabilities pw, pd and pl as long as the odds are announced

    pw = r / ow
    pd = r / od
    pl = r / ol

## Back to The Real World

We have done the above calculations based on the belief: the bookmaker just get the up-front as their benefit. However, this belief doesn't always turn out true (or... it may never become true). In the real world, the bookmaker is usually not satisfied with the "up-front" as the only benefit source. On the other hand, the competition among the bookmakers put pressure on keeping the return rate at the low levels. With all the motivations, the bookmaker chooses odds shifted from the "fair bet" calculations (the one we introduced ahead this section).

Once again, let's dicuss the bookmaker's strategy with an example. Say there is a game "host A v.s. guest B", and by the calculation of "fair bet" odds, we get ow, od and ol as the resulting numbers, and consequently the return rate r is determined. However, instead of annoucing ow, od and ol, the bookmaker announced three slightly different numbers ow', od' and ol', which leads to return rate r' (r' is usually higher than r, to attract more bettors).

Recall that we calculate r' based on the assumption : the bookmaker wants the payout for all three results equal to w * r'. However, in the actual case, with some "tips", bookmaker prefers result "host A wins", and thus he sets

    ow' * ww = w * r''

with r'' < r'. Thus ow' < w * r' / ww. Recall the calculation of the return rate

    r' = 1 / (1 / ow' + 1 / od' + 1 / ol')

To achieve the resulting rate r' with a smaller ow', the bookmaker would raise the value of od' or ol'. As a result, when the bettors believe the return rate is r', the actural return rate of bookmaker is r'' < r' as long as "host A wins". On the other hand, since the value of od' (or ol') has been raised, the actural return rate of bookmaker is higher than r', if "draw game" (or "host A loses"). This is the deep motivation for the bookmaker to derive the "correct" prediction about the game's result, since by "placing the wager" on the correct side, he can earn more money while announcing a high (and hence competitive) return rate.
