import dataclasses
import pandas as pd
import numpy as np


@dataclasses.dataclass
class PcaResult:
    factor: pd.DataFrame
    variance_residual: pd.Series
    embeddings: pd.DataFrame
    input_variance: pd.Series
    factor_covariance: pd.DataFrame


def pca(data, factor_count, name):
    input_means = data.mean()
    input_stds = data.std()
    input_variance = data.var()

    centered_data = data - input_means
    sample_correlation_matrix = centered_data.corr()

    eigenvalues, eigenvectors = np.linalg.eigh(sample_correlation_matrix)
    principal_components = eigenvectors[:, -factor_count:]
    principal_eigenvalues = np.diag(eigenvalues[-factor_count:])
    np_embedding = np.atleast_2d(np.diag(input_stds)) @ principal_components
    np_projection = np.atleast_2d(np.diag(1 / input_stds)) @ principal_components

    factor_names = [f'{name}_{i}' for i in range(1, factor_count + 1)]

    embeddings = pd.DataFrame(np_embedding, columns=factor_names, index=data.columns)
    np_factors = data @ np_projection
    factors = pd.DataFrame(data=np_factors.values, index=data.index, columns=factor_names)
    factor_covariance = pd.DataFrame(principal_eigenvalues, index=factor_names, columns=factor_names)

    projections = centered_data @ np_projection @ np_embedding.T
    residuals = centered_data.values - projections
    np_variance_of_residuals = np.diag(
        np.atleast_2d(
            np.cov(residuals, rowvar=False, ddof=0)
        )
    )
    variance_of_residuals = pd.Series(np_variance_of_residuals, index=data.columns)
    return PcaResult(
        factor=factors,
        variance_residual=variance_of_residuals,
        embeddings=embeddings,
        input_variance=input_variance,
        factor_covariance=factor_covariance
    )

def  main():
        # node1
    corrcoef1 = np.array(
        [
            [1.0, 0.8, 0.0],
            [0.8, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ]
    )
    chol1 = np.linalg.cholesky(corrcoef1)

    data1 = pd.DataFrame(np.random.randn(10000, 3) @ chol1, columns=["1_1", "1_2", "1_3"])

    result1 = pca(data1, factor_count=1, name="Node1")
    factor1 = result1.factor
    embeddings1 = result1.embeddings

    print(data1.corr())

    # node2
    corrcoef2 = np.array(
        [
            [1.0, 0.0, 0.6, 0.3, 0.1, 0.0],
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [0.6, 0.0, 1.0, 0.0, 0.0, 0.0],
            [0.3, 0.0, 0.0, 1.0, 0.0, 0.0],
            [0.1, 0.0, 0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
        ]
    )
    chol2 = np.linalg.cholesky(corrcoef2)

    data2 = pd.DataFrame(np.random.randn(10000, 6) @ chol2, columns=["2_1", "2_2", "2_3", "2_4", "2_5", "2_6"])

    print(data2.corr())

    result2 = pca(data2, factor_count=2, name="Node2")
    factor2 = result2.factor
    embeddings2 = result2.embeddings

    # node3
    corrcoef3 = np.array(
        [
            [1.0, 0.0, 0.8, 0.5, 0.2, 0.0],
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [0.8, 0.0, 1.0, 0.0, 0.0, 0.0],
            [0.5, 0.0, 0.0, 1.0, 0.0, 0.0],
            [0.2, 0.0, 0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
        ]
    )
    chol3 = np.linalg.cholesky(corrcoef3)

    data3 = pd.DataFrame(np.random.randn(10000, 6) @ chol3, columns=["3_1", "3_2", "3_3", "3_4", "3_5", "3_6"])

    print(data3.corr())

    result3 = pca(data3, factor_count=3, name="Node3")
    factor3 = result3.factor
    embeddings3 = result3.embeddings


    data = pd.concat([factor1, factor2, factor3], axis=1)
    result = pca(data, factor_count=4, name="Root")
    embeddings = result.embeddings

    vcv = result.factor_covariance

    vcv_1_modeled = embeddings @ vcv @ embeddings.T + pd.DataFrame(
        np.diag(result.variance_residual), columns=result.variance_residual.index, index=result.variance_residual.index
    )
    vcv_1_modeled_diag = pd.DataFrame(np.diag(np.diag(vcv_1_modeled)), columns=vcv_1_modeled.columns,
                                      index=vcv_1_modeled.index)


    vcv_1_real = data.cov()
    recalculated_residual = result.input_variance[vcv_1_modeled.columns] - np.diag(vcv_1_modeled)
    for diff in recalculated_residual:
        if diff < 0:
            print(f"!!!!!!!!!!!{recalculated_residual}")


    vcv_node_1 = embeddings1 @ vcv_1_modeled.loc[embeddings1.columns, embeddings1.columns] @ embeddings1.T
    recalculated_residual = result1.input_variance[vcv_node_1.columns] - np.diag(vcv_node_1)
    print(f"Node1: {recalculated_residual}")
    for diff in recalculated_residual:
        if diff < 0:
            print(f"!!!!!!!!!!!{recalculated_residual}")

    vcv_node_2 = embeddings2 @ vcv_1_modeled.loc[embeddings2.columns, embeddings2.columns] @ embeddings2.T
    recalculated_residual = result2.input_variance[vcv_node_2.columns] - np.diag(vcv_node_2)
    print(f"Node2: {recalculated_residual}")
    for diff in recalculated_residual:
        if diff < 0:
            print(f"!!!!!!!!!!!{recalculated_residual}")


    vcv_node_3 = embeddings3 @ vcv_1_modeled.loc[embeddings3.columns, embeddings3.columns] @ embeddings3.T
    recalculated_residual = result3.input_variance[vcv_node_3.columns] - np.diag(vcv_node_3)
    print(f"Node3: {recalculated_residual}")
    for diff in recalculated_residual:
        if diff < 0:
            print(f"!!!!!!!!!!!{recalculated_residual}")


if __name__ == "__main__":
    main()








