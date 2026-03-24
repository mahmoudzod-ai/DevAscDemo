class Feature:
    """A basic feature class."""
    
    def __init__(self, name: str):
        self.name = name
    
    def execute(self) -> str:
        """Execute the feature and return a result."""
        return f"Feature '{self.name}' executed successfully"


def main():
    """Main entry point."""
    feature = Feature("myfeature")
    result = feature.execute()
    print(result)


if __name__ == "__main__":
    main()