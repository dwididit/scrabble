from data import letters, points, player_to_words

letter_to_points = zip(letters, points)

letter_to_points = {letters:points for letters, points in letter_to_points}

letter_to_points[" "] = 0

def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter.upper(), 0)
    return point_total

brownie_points = score_word("brownie")

player_to_points = {}


for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        for letter in word:
            player_points += letter_to_points.get(letter.upper(), 0)
    player_to_points[player] = player_points
print(player_to_points)





