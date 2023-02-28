from src.utilities.ilp_manager import *
from src.utilities.cdfg_manager import *
import matplotlib.pyplot as plt
import re
import logging

# function to do sqrt in trivial way
def sqrt(n):
	i = 0
	while (i*i) < n:
		i+=1
	return i

############################################################################################################################################
############################################################################################################################################
#
#	`SCHEDULER` CLASS
#
############################################################################################################################################
#	DESCRIPTION:
#					The following class is used as a scheduler a CDFG (Control DataFlow Graph) representing a function. 
#					It elaborates the CDFG of an IR (Intermediare Representation).
#					Then, it generates its scheduling depending on the scheduling technique selected
############################################################################################################################################
#	ATTRIBUTES:
#					- parser : parser used to generate CDFG after parsing SSA IR
#					- cdfg : CDFG representation of the SSA IR input
#					- cfg : CFG representation of the SSA IR input
#					- sched_tech : scheduling technique selected
#					- sched_sol : scheduling solution
#					- ilp: ilp object
#					- constraints: constraints object
#					- opt_fun: optmization function object
#					- II : Initiation Interval achieved by scheduling solution
#					- log: logger object used to output logs
############################################################################################################################################
#	FUNCTIONS:
#					- set_sched_technique : set scheduling technique
#					- add_artificial_nodes : create super nodes
#					- set_data_dependency_constraints: setting the data dependency constraints
#					- set_II_constraints: setting the initialization interval to the value II_value
#					- add_max_latency_constraint : add max_latency constraint and optimization
#					- add_sink_delays_constraints : add sink delays constraints
#					- set_opt_function: setting the optimiztion function, according to the optimization option
#					- create_scheduling_ilp : create the ILP of the scheduling
#					- solve_scheduling_ilp: solve the ilp and obtain scheduling
#					- get_ilp_tuple : get ilp, constraints and optimization function
#					- get_sink_delays: get delays of sinks after computing solution
#					- print_gantt_chart : prints the gantt chart of a scheduling solution
#					- print_scheduling_summary: it prints the start time of each node into a txt report. If the loop is pipelined, it also prints the achieved II.
############################################################################################################################################
############################################################################################################################################


scheduling_techniques = ["asap", "alap", "pipelined"]

class Scheduler:

	# initialization of the scheduler with the parser
	def __init__(self, parser, sched_technique, log=None):
		if log != None:
			self.log = log
		else:
			self.log = logging.getLogger('scheduler') # if the logger is not given at object generation, create a new one
		self.parser = parser
		self.cdfg = parser.get_cdfg()
		self.cfg = parser.get_cfg()
		self.add_artificial_nodes() # adding supersource and supersinks to the cdfg
		self.set_sched_technique(sched_technique)
		self.sched_sol = None
		self.II = None

		# set solver options
		self.ilp = ILP(log=log)
		self.constraints = Constraint_Set(self.ilp, log=log)
		self.opt_fun = Opt_Function(self.ilp, log=log)

		# define ilp variable per each node
		# TODO: write your code here
		pass

	# function to set scheduling technique
	def set_sched_technique(self, technique):
		assert(technique in scheduling_techniques) # the scheduling technique chosen must belong to the allowed ones
		self.log.info(f'Setting the scheduling technique to be "{technique}"')
		self.sched_tech = technique

	# function for setting the data dependency constraints
	def set_data_dependency_constraints(self, break_bb_connections=False):
		# TODO: write your code here
		pass


	# function for setting the initialization interval to the value II_value
	def set_II_constraints(self, II_value):
		# TODO: write your code here
		pass

	# function to add max_latency constraint and optimization
	def add_max_latency_constraint(self):
		# TODO: write your code here
		pass

	# function to add sink delays constraints
	def add_sink_delays_constraints(self, sink_delays):
		# TODO: write your code here
		pass

		# function to get ilp, constraints and optimization function
	def get_ilp_tuple(self):
		# TODO: write your code here
		pass

	# function to get delays of sinks after computing solution
	def get_sink_delays(self):
		# TODO: write your code here
		pass

	# function to create super nodes
	def add_artificial_nodes(self):
		# TODO: write your code here
		pass

	# function for setting the optimiztion function, according to the optimization option
	def set_opt_function(self):
		if self.sched_tech == 'asap':
			# TODO: write your code here
			pass
		elif self.sched_tech == 'alap':
			# TODO: write your code here
			pass
		elif self.sched_tech == 'pipelined':
			# TODO: write your code here
			pass
		else:
			self.log.error(f'Not implemented option! {self.sched_tech}')
			raise NotImplementedError

	# function to create the ILP of the scheduling
	def create_scheduling_ilp(self, sink_delays=None):
		if self.sched_tech == "asap":
			# TODO: write your code here
			pass
		elif self.sched_tech == "alap":
			# TODO: write your code here
			pass
		elif self.sched_tech == "pipelined":
			# TODO: write your code here
			pass
		self.set_opt_function()

#### DO NOT TOUCH FROM THIS LINE ####

	# function to solve the ilp and obtain scheduling
	def solve_scheduling_ilp(self, base_path, example_name):
		# log the result
		self.ilp.print_ilp("{0}/{1}/output.lp".format(base_path, example_name))
		res = self.ilp.solve_ilp()
		if res != 1:
			self.log.warn("The ILP problem cannot be solved")
			return res
		self.sched_sol = self.ilp.get_ilp_solution() # save solution in an attribute
		# iterate through the different variables to obtain results
		for var, value in self.ilp.get_ilp_solution().items():
			node_type = 'AUX'
			# check if the node represents a timing
			if re.search(r'^sv', var):
				node_name = re.sub(r'^sv', '', var)
				attributes = self.cdfg.get_node(node_name).attr
				node_type = attributes['type']
				attributes['label'] = attributes['label'] + '\n' + f'[{value}]'
				attributes['latency'] = value
			self.log.debug(f'{var} of type {node_type}:= {value}')
		self.cdfg.draw("test_dag_result.pdf", prog="dot")
		if 'max_latency' in self.ilp.get_ilp_solution():
			self.log.info(f'The maximum latency for this cdfg is {self.ilp.get_ilp_solution()["max_latency"]}')
		elif 'max_II' in self.ilp.get_ilp_solution():
			self.log.info(f'The maximum II for this cdfg is {self.ilp.get_ilp_solution()["max_II"]}')
			self.II = self.ilp.get_ilp_solution()["max_II"]
		elif 'II' in self.ilp.get_ilp_solution():
			self.log.info(f'The II for this cdfg is {self.ilp.get_ilp_solution()["II"]}')
			self.II = self.ilp.get_ilp_solution()["II"]
		return res

	# function to get the gantt chart of a scheduling 
	def print_scheduling_summary(self, file_path=None):
		assert self.sched_sol != None, "There should be a solution to an ILP before running this function"
		with open(file_path, 'w') as f:
			# sort the summary by BBs, print the starting time of each node
			for id_ in range(len(self.cfg)):
				# sort the summary by starting time of each node
				for node in sorted(get_cdfg_nodes(self.cdfg), key=lambda n : n.attr["latency"]):
					if int(node.attr['id']) == id_:
						f.write(f'sv({node}) @ bb({id_}) := {node.attr["latency"]}\n')
			if self.II != None:
				f.write(f'II := {self.II}')
			else:
				f.write(f'II := N/A')

	# function to get the gantt chart of a scheduling 
	def print_gantt_chart(self, chart_title="Untitled", file_path=None):
		assert self.sched_sol != None, "There should be a solution to an ILP before running this function"
		variables = {}
		start_time = {}
		duration = {}
		latest_tick = {} # variable to find last tick for xlables
		bars_colors = {}
		for node_name in get_cdfg_nodes(self.cdfg):
			if 'label' in self.cdfg.get_node(node_name).attr:
				attributes = self.cdfg.get_node(node_name).attr
				bb_id = attributes['id']
				if not(bb_id in variables):
					variables[bb_id] = []
					start_time[bb_id] = []
					duration[bb_id] = []
					bars_colors[bb_id] = []
					latest_tick[bb_id] = 0
				variables[bb_id].append(node_name)
				start_time[bb_id].append(float(attributes['latency'])) # start time of each operation
				node_latency = float(get_node_latency(attributes))
				if node_latency == 0.0:
					node_latency = 0.1
					bars_colors[bb_id].append("firebrick")
				else:
					bars_colors[bb_id].append("dodgerblue")
				duration[bb_id].append(node_latency) # duration of each operation
				tmp_tick = float(attributes['latency']) + float(get_node_latency(attributes))
				if tmp_tick > latest_tick[bb_id]:
					latest_tick[bb_id] = tmp_tick
		graphs_per_row = sqrt(len(variables))
		#fig, axs = plt.subplots(int(len(variables)))
		fig = plt.figure(figsize=(20 * 1.5, 11.25 * 1.5), layout='constrained')
		axs=[]
		subplot_format = (graphs_per_row * 110) + 1

		axs_id = 0
		for bb_id in variables:
			axs.append(fig.add_subplot(subplot_format))
			subplot_format += 1
			axs[axs_id].barh(y=variables[bb_id], left=start_time[bb_id], width=duration[bb_id], color=bars_colors[bb_id])
			axs[axs_id].grid()
			axs[axs_id].set_xticks([i for i in range(int(latest_tick[bb_id])+1)])
			axs[axs_id].title.set_text("BB {}".format(bb_id))
			#if self.II != None: # adding II information on the plot
			#	axs[axs_id].hlines(y=-1, xmin=0, xmax=self.II, color='r', linestyle = '-')
			#	axs[axs_id].text(self.II/2-0.35, -2, "II = {0}".format(int(self.II)), color='r')
			axs_id += 1
		#plt.title(chart_title)
		if file_path != None:
			plt.savefig(file_path)
		plt.show()
