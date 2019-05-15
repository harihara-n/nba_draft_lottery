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


def get_file_input():
	teams = []
	print '\nInput file should be csv format with team name,lottery pick percentage in each line.'
	input_file_path = raw_input('Enter file path: ')
	with open(input_file_path) as file:
		for line in file:
			parts = line.strip().split(",")
			teams.append(TeamPercentage(parts[0], int(parts[1])))
	return teams


def get_console_input():
	num_teams = int(raw_input('\nEnter the number of teams: '))
	teams = []
	print '\nWill now prompt you to enter the {} teams in draft order'.format(num_teams)
	for num_team in xrange(num_teams):
		team_name = raw_input('\nEnter team #{} name: '.format(num_team + 1))
		team_lottery_pick_percentage = int(raw_input("Enter {}'s lottery pick percentage: ".format(team_name)))
		teams.append(TeamPercentage(team_name, team_lottery_pick_percentage))
	return teams

def verify_teams_input(teams):
	sum_lottery_pick_percentages = sum([team.team_lottery_pick_percentage for team in teams])
	if sum_lottery_pick_percentages != 100:
		raise Exception('Lottery pick percentages of teams: {} is not 100'.format(sum_lottery_pick_percentages))

def get_num_lottery_picks_input(num_teams):
	num_lottery_picks = int(raw_input('\nEnter the number of lottery picks: '))
	if num_lottery_picks > num_teams:
		raise Exception(
			'Number of lottery picks: {} cannot be greater than the number of teams: {}'.format(
				num_lottery_picks, num_teams
			)
		)
	return num_lottery_picks


if __name__ == '__main__':
	print 'Welcome to the NBA Lottery Draft Generator'
	print '###########################################'

	input_option = raw_input('\nEnter 1 to read team input from a file or anything else to type input into the console: ').strip()
	if input_option == '1':
		teams = get_file_input()
	else:
		teams = get_console_input()

	verify_teams_input(teams)

	num_lottery_picks = get_num_lottery_picks_input(len(teams))

	draft_order = generate_draft_order(teams, num_lottery_picks)
	print '\nGenerated Draft Order'
	print '########################'
	for team in draft_order:
		print team
	print '\n'
