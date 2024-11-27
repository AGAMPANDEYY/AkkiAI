from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
import os
#from langchain_anthropic import ChatAnthropic

# Uncomment the following line to use an example of a custom tool
# from akkiai.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class Akkiai():
    """Akkiai crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    claude_llm=LLM(api_key=os.getenv("ANTHROPIC_API_KEY"), model="claude-3",stream=True)
    #ChatAnthropic(model_name="claude-3",streaming=True,api_key=os.getenv("ANTHROPIC_API_KEY"))
    print(claude_llm)
    
    def llm(self):
        return LLM(api_key=os.getenv("ANTHROPIC_API_KEY"), model="claude-3",stream=True)
    @before_kickoff # Optional hook to be executed before the crew starts
    def pull_data_example(self, inputs):
        # Example of pulling data from an external API, dynamically changing the inputs
        inputs['extra_data'] = "This is extra data"
        return inputs

    @after_kickoff # Optional hook to be executed after the crew has finished
    def log_results(self, output):
        # Example of logging results, dynamically changing the output
        print(f"Results: {output}")
        return output
    
    #Agent1
    @agent
    def TargetAudienceAgent(self) -> Agent:
        return Agent(
            config=self.agents_config['TargetAudienceAgent'],
            # tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
            #llm=self.claude_llm,
            #llm='claude-2',
            #llm=self.llm(),
            #verbose=True
        )

    #Agent2
    @agent
    def BuyerPersonaAgent(self) -> Agent:
        return Agent(
            config=self.agents_config['BuyerPersonaAgent'],
            #llm=LLM(api_key=os.getenv("ANTHROPIC_API_KEY"), model="claude-3-5-sonnet-20240620" ),
            #llm=self.claude_llm,
            #llm='claude-2',
            #llm=self.llm(),
            #verbose=True
        )
    
    #Agent3
    @agent
    def B2CPersonaAnalystAgent(self) -> Agent:
        return Agent(
            config=self.agents_config['B2CPersonaAnalystAgent'],
            #llm=LLM(api_key=os.getenv("ANTHROPIC_API_KEY"), model="claude-3-5-sonnet-20240620" ),
            #llm=self.claude_llm,
            #llm='claude-2',
            #llm=self.llm(),
            #verbose=True
        )
    #Agent4
    @agent
    def B2BPersonaAnalystAgent(self) -> Agent:
        return Agent(
            config=self.agents_config['B2BPersonaAnalystAgent'],
            #llm=LLM(api_key=os.getenv("ANTHROPIC_API_KEY"), model="claude-3-5-sonnet-20240620" ),
            #llm=self.claude_llm,
            #llm='claude-2',
            #llm=self.llm(),
            #verbose=True
        )
    #Agent5
    @agent
    def JTBDAnalysisAgent(self) -> Agent:
        return Agent(
            config=self.agents_config['JTBDAnalysisAgent'],
            #llm=LLM(api_key=os.getenv("ANTHROPIC_API_KEY"), model="claude-3-5-sonnet-20240620" ),
            #llm=self.claude_llm,
            #llm='claude-2',
            #llm=self.llm(),
            #verbose=True
        )
    #Agent6
    @agent
    def StagesofAwarenessAgent(self) -> Agent:
        return Agent(
            config=self.agents_config['StagesofAwarenessAgent'],
            #llm=LLM(api_key=os.getenv("ANTHROPIC_API_KEY"), model="claude-3-5-sonnet-20240620"),
            #llm=self.claude_llm,
            #llm=self.llm(),
            #verbose=True
        )

    #Agent7
    @agent
    def TGAnalysisAgent(self) -> Agent:
        return Agent(
            config=self.agents_config['TGAnalysisAgent'],
            #llm=LLM(api_key=os.getenv("ANTHROPIC_API_KEY"), model="claude-3-5-sonnet-20240620",stream=True ),
            #llm=self.claude_llm,
            #llm='claude-2',
            #llm=self.llm(),
            #verbose=True
        )
    #task1
    @task
    def TargetAudienceAgent_task(self) -> Task:
        return Task(
            config=self.tasks_config['finding_target_audience'],
        )

    #task2
    @task
    def BuyerPersonaAgent_task(self) -> Task:
        return Task(
            config=self.tasks_config['creating_buyer_persona'],
            input_file='persona_input.txt',
        )

    #task3
    @task
    def B2CPersonaAnalystAgent_task(self) -> Task:
        return Task(
            config=self.tasks_config['creating_b2c_persona'],
            input_file='persona_input.txt',
        )

    #task4
    @task
    def B2BPersonaAnalystAgent_task(self) -> Task:
        return Task(
            config=self.tasks_config['creating_b2b_persona'],
            input_file='persona_input.txt',
        )
 
    #task5
    @task
    def JTBDAnalysisAgent_task(self) -> Task:
        return Task(
            config=self.tasks_config['analysing_jtbd'],
            input_file='jtbd_input.txt',
        )
    
    #task6
    @task
    def StagesofAwarenessAgent_task(self) -> Task:
        return Task(
            config=self.tasks_config['analysing_stages_of_awareness'],
            input_file='awareness_input.txt',
        )

    #task7
    @task
    def TGAnalysisAgent_task(self) -> Task:
        return Task(
            config=self.tasks_config['analysing_TG'],
            input_file='tg_input.txt',
            output_file='tg_output.txt'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AkkiAi crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )