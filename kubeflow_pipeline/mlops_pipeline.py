import kfp
from kfp import dsl  # to define steps in pipeline

# Components
def data_processing_op():
    return dsl.ContainerOp(
        name = "Data_Processing",
        image = "rajasekhar8995/my-mlops-project-5-app:latest",
        command = ["python", "src/data_processing.py"]
    )


def model_training_op():
    return dsl.ContainerOp(
        name = "Model_Training",
        image = "rajasekhar8995/my-mlops-project-5-app:latest",
        command = ["python", "src/model_training.py"]
    )

# Pipeline creation

@dsl.pipeline(
    name="MLOps Pipeline",
    description = "My first kubeflow pipeline"

)

def mlops_pipeline():
    data_processing = data_processing_op()
    model_training = model_training_op().after(data_processing)


# Run the pipeline

if __name__ == "__main__":
    kfp.compiler.Compiler().compile(
        mlops_pipeline, "mlops_pipeline.yaml"
    )