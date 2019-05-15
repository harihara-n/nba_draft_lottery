from numpy.random import choice

class TeamPercentage(object):
	def __init__(self, team_name, team_lottery_pick_percentage):
		self.team_name = team_name
		self.team_lottery_pick_percentage = team_lottery_pick_percentage

def generate_draft_order(teams, num_lottery_picks):
	draft_order = []
	teams_copy = list(teams)
	for lottery_pick in xrange(num_lottery_picks):
		chosen_team = choice([team.team_name for team in teams_copy], 1, [team.team_lottery_pick_percentage for team in teams_copy])
		draft_order.append(chosen_team[0])
		for index, team in enumerate(teams_copy):
			if team.team_name == chosen_team:
				del teams_copy[index]
				break

	teams_copy = filter(lambda team: team.team_name not in draft_order, teams_copy)
	return draft_order + [team.team_name for team in teams_copy]

def get_file_input():
	teams = []
	print '\nInput file should be csv format with team name,lottery pick percentage in each line.'
	input_file_path = raw_input('Enter file path: ')
	with open(input_file_path) as file:
		for line in file:
			parts = line.strip().split(",")
			teams.append(TeamPercentage(parts[0], float(parts[1])))
	return teams

def get_console_input():
	num_teams = int(raw_input('\nEnter the number of teams: '))
	teams = []
	print '\nWill now prompt you to enter the {} teams in draft order'.format(num_teams)
	for num_team in xrange(num_teams):
		team_name = raw_input('\nEnter team #{} name: '.format(num_team + 1))
		team_lottery_pick_percentage = float(raw_input("Enter {}'s lottery pick percentage: ".format(team_name)))
		teams.append(TeamPercentage(team_name, team_lottery_pick_percentage))
	return teams

def verify_and_process_teams_input(teams):
	sum_lottery_pick_percentages = sum([team.team_lottery_pick_percentage for team in teams])
	if sum_lottery_pick_percentages != 100:
		raise Exception('Lottery pick percentages of teams: {} is not 100'.format(sum_lottery_pick_percentages))

	return map(lambda team: TeamPercentage(team.team_name, team.team_lottery_pick_percentage / 100.0), teams)

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

	teams = verify_and_process_teams_input(teams)

	num_lottery_picks = get_num_lottery_picks_input(len(teams))

	draft_order = generate_draft_order(teams, num_lottery_picks)
	print '\nGenerated Draft Order'
	print '########################'
	for team in draft_order:
		print team
	print '\n'
