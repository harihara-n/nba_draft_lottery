import random

class TeamPercentage(object):
	def __init__(self, team_name, team_lottery_pick_percentage):
		self.team_name = team_name
		self.team_lottery_pick_percentage = team_lottery_pick_percentage

def generate_draft_order(teams, num_lottery_picks):
	teams_list = []
	for team in teams:
		teams_list = teams_list + ([team.team_name] * team.team_lottery_pick_percentage)

	random.seed()
	draft_order = []
	for lottery_pick_num in xrange(num_lottery_picks):
		random_number = random.randint(0, len(teams_list) - 1)
		chosen_team = teams_list[random_number]
		draft_order.append(chosen_team)
		teams_list = filter(lambda team: team != chosen_team, teams_list)

	teams = filter(lambda team: team.team_name not in draft_order, teams)
	return draft_order + [team.team_name for team in teams]


if __name__ == '__main__':
	num_teams = int(raw_input('\nEnter the number of teams: '))
	teams = []
	print '\nWill now prompt you to enter the {} teams in draft order'.format(num_teams)
	for num_team in xrange(num_teams):
		team_name = raw_input('\nEnter team #{} name: '.format(num_team + 1))
		team_lottery_pick_percentage = int(raw_input("Enter {}'s lottery pick percentage: ".format(team_name)))
		teams.append(TeamPercentage(team_name, team_lottery_pick_percentage))

	sum_lottery_pick_percentages = sum([team.team_lottery_pick_percentage for team in teams])
	if sum_lottery_pick_percentages != 100:
		raise Exception('Lottery pick percentages of teams: {} is not 100'.format(sum_lottery_pick_percentages))

	num_lottery_picks = int(raw_input('\nEnter the number of lottery picks: '))
	if num_lottery_picks > num_teams:
		raise Exception(
			'Number of lottery picks: {} cannot be greater than the number of teams: {}'.format(
				num_lottery_picks, num_teams
			)
		)

	draft_order = generate_draft_order(teams, num_lottery_picks)
	print 'Draft Order'
	print '########################'
	for team in draft_order:
		print team
