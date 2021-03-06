
set -euo pipefail
SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
[[ -n "${DEBUG:-}" ]] && set -x

log() { echo "$1" >&2; }

TAG="${TAG:?TAG env variable must be specified}"
REPO_PREFIX="${REPO_PREFIX:?REPO_PREFIX env variable must be specified}"
OUT_DIR="${OUT_DIR:-${SCRIPTDIR}/../release}"



print_autogenerated_warning() {
    cat<<EOF
# ----------------------------------------------------------
# WARNING: This file is autogenerated. Do not manually edit.
# ----------------------------------------------------------
EOF
}

# define gsed as a function on Linux for compatibility
[ "$(uname -s)" == "Linux" ] && gsed() {
    sed "$@"
}

read_manifests() {
    local dir
    dir="$1"

    while IFS= read -d $'\0' -r file; do
        # strip license headers (pattern "^# ")
        awk '
        /^[^# ]/ { found = 1 }
        found { print }' "${file}"

        echo "---"
    done < <(find "${dir}" -name '*.yaml' -type f -print0)
}

mk_kubernetes_manifests() {
    out_manifest="$(read_manifests "${SCRIPTDIR}/../kubernetes-manifests")"

    # replace "image" repo, tag for each service
    for dir in ./src/*/
    do
        svcname="$(basename "${dir}")"
        image="$REPO_PREFIX/$svcname:$TAG"

        pattern="^(\s*)image:\s.*$svcname(.*)(\s*)"
        replace="\1image: $image\3"
        out_manifest="$(gsed -r "s|$pattern|$replace|g" <(echo "${out_manifest}") )"
    done


    print_autogenerated_warning
    echo "${out_manifest}"
}

mk_istio_manifests() {
    print_autogenerated_warning
    read_manifests "${SCRIPTDIR}/../istio-manifests"
}

main() {
    mkdir -p "${OUT_DIR}"
    local k8s_manifests_file istio_manifests_file

    k8s_manifests_file="${OUT_DIR}/kubernetes-manifests.yaml"
    mk_kubernetes_manifests > "${k8s_manifests_file}"
    log "Written ${k8s_manifests_file}"

    istio_manifests_file="${OUT_DIR}/istio-manifests.yaml"
    mk_istio_manifests > "${istio_manifests_file}"
    log "Written ${istio_manifests_file}"
}

main