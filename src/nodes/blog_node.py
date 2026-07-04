from src.states.blogstate import BlogState
from langchain_core.messages import HumanMessage
from src.states.blogstate import Blog

class BlogNode:
    """
    A class to represent he blog node
    """

    def __init__(self, llm):
        self.llm = llm

    def _get_language(self, state: BlogState) -> str:
        return (state.get("current_language") or state.get("language") or "english").lower()

    def title_creation(self, state: BlogState):
        """
        create the title for the blog
        """
        if "topic" in state and state["topic"]:
            requested_language = self._get_language(state)
            prompt = f"""
            You are an expert blog content writer. Use Markdown formatting. Generate
            a blog title for the topic: {state['topic']}. This title should be creative and SEO friendly.
            Write the title in {requested_language}.
            """
            response = self.llm.invoke(prompt)
            return {"blog": {"title": response.content}}

    def content_generation(self, state: BlogState):
        if "topic" in state and state["topic"]:
            requested_language = self._get_language(state)
            system_prompt = f"""You are expert blog writer. Use Markdown formatting.
            Generate a detailed blog content with detailed breakdown for the topic: {state['topic']}.
            Write the content in {requested_language}."""
            response = self.llm.invoke(system_prompt)
            return {"blog": {"title": state.get("blog", {}).get("title", ""), "content": response.content}}

    def translation(self, state: BlogState):
        """
        Translate the content to the specified language.
        """
        requested_language = self._get_language(state)
        translation_prompt = f"""
        Translate the following content into {requested_language}.
        - Maintain the original tone, style, and formatting.
        - Adapt cultural references and idioms to be appropriate for {requested_language}.

        ORIGINAL CONTENT:
        {state['blog']['content']}
        """
        messages = [HumanMessage(content=translation_prompt)]
        translation_content = self.llm.with_structured_output(Blog).invoke(messages)
        return {"blog": {"title": state.get("blog", {}).get("title", ""), "content": translation_content.content}}

    def route(self, state: BlogState):
        return {"current_language": self._get_language(state)}

    def route_decision(self, state: BlogState):
        """
        Route the content to the respective translation function.
        """
        requested_language = self._get_language(state)
        if requested_language == "hindi":
            return "hindi"
        elif requested_language == "french":
            return "french"
        else:
            return "__end__"