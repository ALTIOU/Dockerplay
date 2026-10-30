# Dockerplay

通过 GitHub Actions 手动把 DockerHub 镜像复制到当前仓库所有者的 GitHub 容器注册表（GHCR）。不需要保存 DockerHub 密码或个人访问令牌。

## 使用

1. Fork 或克隆本仓库到自己的 GitHub 账号。如果使用 Fork，先在 **Actions** 页面启用工作流。
2. 打开 **Actions → 将 DockerHub 镜像复制到 GHCR → Run workflow**。
3. 填写参数并运行：

| 参数 | 示例 | 说明 |
| --- | --- | --- |
| `dockerhub_image` | `nginx` 或 `library/nginx` | DockerHub 镜像名，不含标签；使用小写 |
| `tag` | `latest` 或 `1.27-alpine` | 源和目标使用同一标签；留空时为 `latest` |
| `ghcr_image` | `my-nginx` | 目标镜像名；会转换为小写 |

工作流会生成如下目标地址。命名空间使用仓库所有者，不随触发工作流的协作者变化：

```text
ghcr.io/<仓库所有者的小写用户名>/<ghcr_image的小写名称>:<tag>
```

例如，`ALTIOU` 账号下的仓库输入 `nginx`、`latest`、`my-nginx`，输出地址为：

```sh
docker pull ghcr.io/altiou/my-nginx:latest
```

## 权限与可见性

工作流显式申请 `contents: read` 和 `packages: write`，使用 GitHub 为本次运行生成的 `GITHUB_TOKEN` 登录 GHCR。

新建的 GHCR 包可能默认是私有的。需要其他人匿名拉取时，请在包的设置中检查可见性；私有包拉取则需要相应身份和权限。若目标包已经存在，需要确保当前仓库有该包的写入权限。

## 复制范围

当前实现使用 `docker pull/tag/push`，复制 GitHub Runner 当前平台选中的镜像，**不会自动复制上游全部架构**。需要 ARM 镜像或完整多架构清单时，应使用对应平台或支持多架构复制的工具。

复制完成后，目标镜像仍受 GHCR 的可见性、容量和账号权限规则管理。相同目标标签可被后续运行覆盖，必要时使用固定版本标签。

## GitHub Actions 用量

公开仓库使用标准 GitHub 托管 Runner 时，运行器用量免费；私有仓库的包含额度、额外用量及存储按当前账号方案计费。运行时长和其他服务限制仍适用。

- [GitHub Actions 计费说明](https://docs.github.com/en/billing/concepts/product-billing/github-actions)
- [使用 GITHUB_TOKEN 发布容器镜像](https://docs.github.com/en/actions/tutorials/publish-packages/publish-docker-images)
- [GHCR 认证和包可见性](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)

## 来源

原项目说明引用了 [foss-android/dockerhub2ghcr.io](https://github.com/foss-android/dockerhub2ghcr.io)。本仓库保留该来源说明。
