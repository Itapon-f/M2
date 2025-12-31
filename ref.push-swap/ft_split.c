/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: agiron-d <agiron-d@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 02:27:56 by agiron-d          #+#    #+#             */
/*   Updated: 2025/12/02 03:16:38 by agiron-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	ft_count_words(const char *str)
{
	int	count;
	int	in_word;
	int	i;

	count = 0;
	in_word = 0;
	i = 0;
	while (str[i])
	{
		if (!ft_is_space(str[i]) && !in_word)
		{
			count++;
			in_word = 1;
		}
		else if (ft_is_space(str[i]))
			in_word = 0;
		i++;
	}
	return (count);
}

static char	*ft_strndup(const char *str, int n)
{
	char	*copy;
	int		j;
	int		len;

	j = 0;
	len = 0;
	if (!str)
		return (NULL);
	while (str[len] && len < n)
		len++;
	copy = malloc((len + 1) * sizeof(char));
	if (!copy)
		return (NULL);
	while (j < len)
	{
		copy[j] = str[j];
		j++;
	}
	copy[len] = 0;
	return (copy);
}

void	ft_split_free(char **lst)
{
	int	i;

	i = 0;
	while (lst[i])
		free(lst[i++]);
	free(lst);
}

static void	ft_fill_result(char *str, char **result, int *i, int *j)
{
	int	start;

	start = *i;
	while (str[*i] && !ft_is_space(str[*i]))
		(*i)++;
	result[(*j)++] = ft_strndup(str + start, *i - start);
}

char	**ft_split(char *str)
{
	int		i;
	int		j;
	char	**result;

	result = malloc((ft_count_words(str) + 1) * sizeof(char *));
	if (!str || !result)
		return (NULL);
	i = 0;
	j = 0;
	while (str[i])
	{
		if (ft_is_space(str[i]))
			i++;
		else
			ft_fill_result(str, result, &i, &j);
	}
	result[j] = NULL;
	return (result);
}
